import comtypes
import numpy as np

comtypes.CoInitialize()

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


class AudioController:
    def __init__(self):
        # ✅ FIX: directly get default audio endpoint (correct way)
        devices = AudioUtilities.GetSpeakers()

        # ⚠️ SAFE WAY: enumerate real endpoint correctly
        interface = AudioUtilities.GetDeviceEnumerator().GetDefaultAudioEndpoint(0, 1)

        self.volume = interface.Activate(
            IAudioEndpointVolume._iid_,
            CLSCTX_ALL,
            None
        )

        self.volume = cast(self.volume, POINTER(IAudioEndpointVolume))

        self.min_vol, self.max_vol = self.volume.GetVolumeRange()[:2]

        self.last_volume = 0

    def set_volume(self, distance):
        target = np.interp(distance, [30, 200], [0, 100])

        smoothed = self.last_volume * 0.8 + target * 0.2
        self.last_volume = smoothed

        vol = np.interp(smoothed, [0, 100], [self.min_vol, self.max_vol])

        self.volume.SetMasterVolumeLevel(vol, None)

        return int(smoothed)
