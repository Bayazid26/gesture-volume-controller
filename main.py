import cv2

from audio_controller import AudioController
from gesture_detector import GestureDetector
from utils import calculate_distance, SmoothFilter

cap = cv2.VideoCapture(0)

detector = GestureDetector()
audio = AudioController()
smooth = SmoothFilter(alpha=0.25)

prev_distance = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    results = detector.process(img)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:

            lm_list = detector.get_landmarks(img, handLms)

            if lm_list:
                x1, y1 = lm_list[4][1], lm_list[4][2]
                x2, y2 = lm_list[8][1], lm_list[8][2]

                distance = calculate_distance((x1, y1), (x2, y2))

                # 🧠 SMART FILTER: ignore noise
                if abs(distance - prev_distance) > 2:
                    filtered = smooth.update(distance)
                    vol = audio.set_volume(filtered)
                    prev_distance = distance
                else:
                    vol = audio.last_volume

                # 🎯 UI feedback (cleaner)
                cv2.circle(img, (x1, y1), 10, (0, 255, 0), -1)
                cv2.circle(img, (x2, y2), 10, (0, 255, 0), -1)
                cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

                cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 2)
                bar = int(400 - (vol * 2.5))
                cv2.rectangle(img, (50, bar), (85, 400), (255, 0, 0), -1)

                cv2.putText(img, f'Volume: {vol}%',
                            (50, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            (0, 255, 0),
                            2)

    cv2.imshow("SMART Gesture Volume Control", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
