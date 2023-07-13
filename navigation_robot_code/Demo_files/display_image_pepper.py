from sic_framework.core.application import SICApplication
from sic_framework.devices.common_naoqi.naoqi_speakers import NaoqiTextToSpeechRequest
from sic_framework.devices.common_naoqi.pepper_tablet import NaoqiTabletService, NaoqiLoadUrl
from sic_framework.devices.pepper import Pepper

from sic_framework.services.webserver.webserver_service import WebserverConf, WebserverService, GetWebText
from sic_framework.devices.common_naoqi.nao_motion import NaoPostureRequest, NaoRestRequest, NaoWakeUpRequest, \
    AnimationRequest

class PepperImage(SICApplication):
    def run(self) -> None:
        pepper = self.connect(Pepper, device_id='pepper')
        pepper_action = self.connect(NaoqiTabletService, device_id='pepper')
        # pepper_action.request(NaoqiLoadUrl('http://)
        print('showing image')
        pepper.tablet_service.showImage('http://192.168.0.1/sic/navigation_robot_code/maps/Floor_plan.png')
