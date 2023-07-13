"""
This file is used to display the start screen (with 'START' button, that starts interaction with the robot) and the Rating screen (with rate buttons/values) on the Pepper's tablet.
"""

import io
import logging
import time

import numpy as np

from sic_framework.core.application import SICApplication, SICAction
from sic_framework.services.webserver.webserver_service import WebserverService, WebserverConf, GetWebText
from sic_framework.services.dialogflow.dialogflow_service import DialogflowService, DialogflowConf, \
    GetIntentRequest, RecognitionResult, QueryResult
# from sic_framework.devices.desktop import Desktop

from sic_framework.devices.nao import Nao
from sic_framework.devices.pepper import Pepper
from sic_framework.devices.common_naoqi.pepper_tablet import NaoqiTabletService, NaoqiLoadUrl
from main_GPT_Robot import GPTPepper
from main_GPT_Robot import read_json
from rating_screen import Rating
import csv
from datetime import datetime


def save_interaction_rating(row):
    with open(r'rating.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(row)


class StartScreen(SICApplication):
    """Example that shows how to use a browser connection (on a Pepper or the computer-browser).
    The webserver service needs to be running for this!"""

    def __init__(self):
        super().__init__()
        self.pepper_tablet_connector = None
        self.webserver_connector = None
        self.chat = GPTPepper()
        self.data = []

    def run(self) -> None:
        """
        Render an HTML file with Bootstrap and a CSS file to a web browser
        """
        web_conf = WebserverConf(host="0.0.0.0", port=8080)
        self.webserver_connector = self.connect(WebserverService, device_id='web', inputs_to_service=[self],
                                                log_level=logging.INFO, conf=web_conf)
        self.pepper_tablet_connector = self.connect(NaoqiTabletService, device_id='pepper',
                                                    inputs_to_service=[self])
        # the HTML file to be rendered
        # html_file = ".html"
        # web_url = "http://192.168.0.208:8080/"
        web_url = "http://10.15.3.120:8080/" # NOTE: Change to system IP address
        # web_url = "http://wikipedia.nl/"
        # web_url = "https://prnt.sc/GNc0gf1hPBBw"

        text = self.get_text('Ask me for directions!')
        start_button = self.get_button('Start')
        html_file = self.get_header() + self.get_body(text + start_button) + self.get_footer()
        # html_file = 'likert.html'
        # html_file = 'Floor_plan_bg.html'

        # send html to WebserverService
        with open(html_file) as file:
            file_data = file.read()
            self.webserver_connector.send_message(GetWebText(file_data))
        # self.webserver_connector.send_message(GetWebText(html_file))

        # send url to NaoqiTabletService in order to display it on a pepper's tablet
        self.pepper_tablet_connector.send_message(NaoqiLoadUrl(web_url))
        time.sleep(3)

        # And now we wait until someone presses the button (see on_browser_button above)

    def on_browser_button(self, button: str) -> None:
        print(button, type(button))
        if button == '<h1 style="font-size:8vw">' + 'Start' + '</h1>':
            self.data.append("Start")
            self.chat.run()
        if button == "1":
            self.data.append("1")
            save_interaction_rating(self.data)
            self.data.clear()
            start_screen.restart()
        elif button == "2":
            self.data.append("2")
            save_interaction_rating(self.data)
            self.data.clear()
            start_screen.restart()
        elif button == "3":
            self.data.append("3")
            save_interaction_rating(self.data)
            self.data.clear()
            start_screen.restart()
        elif button == "4":
            self.data.append("4")
            save_interaction_rating(self.data)
            self.data.clear()
            start_screen.restart()
        elif button == "5":
            self.data.append("5")
            save_interaction_rating(self.data)
            self.data.clear()
            start_screen.restart()
        elif button == "6":
            self.data.append("6")
            save_interaction_rating(self.data)
            self.data.clear()
            start_screen.restart()
        elif button == "7":
            self.data.append("7")
            save_interaction_rating(self.data)
            self.data.clear()
            start_screen.restart()
        else:
            start_screen.restart()
        # print(button + ' pressed, exiting...')
        # self.stop()
        # example = Example('127.0.0.1')
        # example.restart()

    def restart(self) -> None:

        # text = self.get_text('Ask me for directions!')
        # button = self.get_button('Start')
        # html = self.get_header() + self.get_body(text + button) + self.get_footer()

        start_screen.run()

    @staticmethod
    def get_header() -> str:
        """
        A header (navbar) with a listening icon on the left and a VU logo on the right.
        """
        return '<nav class="navbar mb-5">' \
               '<div class="navbar-brand listening_icon"></div>' \
               '<div class="navbar-nav vu_logo"></div>' \
               '</nav>'

    @staticmethod
    def get_body(contents: str) -> str:
        """
        The given contents in a centered container.
        """
        return '<main class="container text-center">' + contents + '</main>'

    @staticmethod
    def get_footer() -> str:
        """
        A footer that shows the currently recognized spoken text (if any).
        """
        return '<footer class="fixed-bottom">' \
               '<p class="lead bg-light text-center speech_text"></p>' \
               '</footer>'

    @staticmethod
    def get_text(txt: str) -> str:
        """
        A simple text display.
        """
        return '<h1 style="font-size:8vw">' + txt + '</h1>'

    @staticmethod
    def get_button(label: str) -> str:
        """
        A clickable button.
        """
        return '<button class="btn btn-primary btn-lg mt-5 ml-3">' + '<h1 style="font-size:8vw">' + label + '</h1>' + '</button>'


start_screen = StartScreen()
start_screen.run()
start_screen.stop()