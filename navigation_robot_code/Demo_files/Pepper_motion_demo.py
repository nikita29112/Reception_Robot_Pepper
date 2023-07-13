import io
import json
import logging
import time

import cv2
import numpy as np
import pyaudio
from sic_framework.core.application import SICApplication
from sic_framework.devices.common_naoqi.nao_motion import NaoPostureRequest, NaoRestRequest, NaoWakeUpRequest
from sic_framework.devices.common_naoqi.naoqi_camera import TopNaoCamera, NaoqiCameraConf
from sic_framework.devices.common_naoqi.naoqi_microphone import NaoqiMicrophone
from sic_framework.devices.common_naoqi.naoqi_speakers import NaoqiTextToSpeechRequest
from sic_framework.devices.desktop.desktop_microphone import DesktopMicrophone
from sic_framework.devices.pepper import Pepper
from sic_framework.devices.common_naoqi.naoqi_motion_recorder import NaoMotionRecorderAction, NaoMotionReplayAction, \
    NaoMotionRecordingStart, NaoMotionRecordingStop, NaoMotionRecordingReplay
from sic_framework.devices.common_naoqi.nao_motion import NaoPostureRequest, NaoRestRequest, NaoWakeUpRequest, AnimationRequest


class PepperMotion(SICApplication):
    def run(self) -> None:
        pepper = Pepper(device_id='pepper', application=self)
        # play_action = self.connect(NaoMotionReplayAction, device_id='pepper', inputs_to_service=[self],
        # log_level=logging.INFO)
        pepper.text_to_speech.request(NaoqiTextToSpeechRequest('Hello!'))
        print('---Ready--')
        # pepper.motion.request(NaoPostureRequest('Stand'))
        # pepper.text_to_speech.request(NaoqiTextToSpeechRequest("I am Pepper. Nice to meet you"))

        pepper.motion.request(NaoPostureRequest('Stand', 0.3))
        print("done")
        pepper.motion.request(AnimationRequest('animations/Stand/Gestures/Hey_1'))
        print("done")
        pepper.motion.request(NaoPostureRequest('Stand'))
        #pepper.motion.request(NaoMotionRecordingReplay(wave_motion_file))
        # play_action.request(NaoMotionRecordingReplay(wave_motion_file))


if __name__ == '__main__':
    test_app = PepperMotion()
    test_app.run()
    test_app.stop()
