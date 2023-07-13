from sic_framework import SICApplication
from sic_framework.devices.pepper import Pepper
from sic_framework.devices.common_naoqi.naoqi_speakers import NaoqiTextToSpeechRequest, NaoqiTextToSpeechAction


class TestPepper(SICApplication):
    def run(self) -> None:
        pepper = Pepper(device_id='pepper', application=self)
        # pepper = self.connect(NaoqiTextToSpeechAction, device_id='pepper')
        pepper.text_to_speech.request(NaoqiTextToSpeechRequest('Hello!'))
        print('---Ready--')
        pepper.text_to_speech.request(NaoqiTextToSpeechRequest("I am Pepper. Nice to meet you"))


if __name__ == '__main__':
    test_app = TestPepper()
    test_app.run()
    test_app.stop()
