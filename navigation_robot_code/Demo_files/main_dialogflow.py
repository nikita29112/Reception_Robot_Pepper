import json
import logging

import numpy as np
import pyaudio

from sic_framework.core.application import SICApplication
from sic_framework.devices.common_naoqi.naoqi_speakers import NaoqiTextToSpeechRequest
from sic_framework.devices.pepper import Pepper
from sic_framework.services.dialogflow.dialogflow_service import DialogflowService, DialogflowConf, GetIntentRequest, \
    RecognitionResult, QueryResult

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100


class DialogflowConv(SICApplication):

    def __init__(self):
        super().__init__()
        self.user_response = None

    def on_dialog(self, message):
        if message.response:
            # print(message.response.recognition_result.transcript)
            if message.response.recognition_result.is_final:
                self.user_response = message.response.recognition_result.transcript
                print('Transcript: ', self.user_response)

                return self.user_response

    def run(self) -> None:
        self.user_response = None
        # nao = Nao(device_id='nao', application=self)
        pepper = Pepper(device_id='pepper', application=self)
        keyfile_json = json.load(open('../dialogflow_keyfile.json'))

        conf = DialogflowConf(keyfile_json=keyfile_json,
                              project_id='dialogflow_project_id', sample_rate_hertz=16000, )
        # mic_service = nao.mic
        mic_service = pepper.mic
        dialogflow = self.connect(DialogflowService, device_id='local', inputs_to_service=[mic_service],
                                  log_level=logging.INFO, conf=conf)

        self.user_response = dialogflow.register_callback(self.on_dialog)

        # nao.text_to_speech.request(NaoqiTextToSpeechRequest('Hello!'))
        pepper.text_to_speech.request(NaoqiTextToSpeechRequest('Hello!'))
        print('--Ready--')

        x = np.random.randint(10000)

        for i in range(25):
            print('---Conversation Turn ----', i)
            reply = dialogflow.request(GetIntentRequest(x))

            if reply.response.query_result.fulfillment_messages:
                text = str(reply.response.query_result.fulfillment_messages[0].text.text[0])
                pepper.text_to_speech.request(NaoqiTextToSpeechRequest(text))
                print("REPLY", text)

            if reply.response.query_result.intent:
                intent_name = reply.response.query_result.intent.display_name
                print(f"INTENT '{intent_name}'")

            print(f'User input: ', self.user_response)
            print(f'User input type: ', type(self.user_response))


if __name__ == '__main__':
    test_app = DialogflowConv()
    test_app.run()
