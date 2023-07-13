from abc import ABC

from sic_framework import SICApplication
from sic_framework import SICAction
from sic_framework.devices.common_naoqi.naoqi_speakers import NaoqiTextToSpeechRequest, NaoqiTextToSpeechAction


class PepperSpeech(SICApplication):
    def run(self) -> None:
        pepper_action = self.connect(NaoqiTextToSpeechAction, device_id='pepper')
        pepper_action.request(NaoqiTextToSpeechRequest('Hi, I am pepper. Nice to meet you!'))


if __name__ == '__main__':
    test_app = PepperSpeech()
    test_app.run()
    test_app.stop()
