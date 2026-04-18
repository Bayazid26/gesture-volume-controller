import cv2
import mediapipe as mp


class GestureDetector:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
        self.draw = mp.solutions.drawing_utils

    def process(self, img):
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return self.hands.process(rgb)

    def get_landmarks(self, img, handLms):
        h, w, _ = img.shape
        lm_list = []

        for id, lm in enumerate(handLms.landmark):
            lm_list.append((id, int(lm.x * w), int(lm.y * h)))

        return lm_list
