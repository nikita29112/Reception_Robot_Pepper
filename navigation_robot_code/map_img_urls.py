"""
This file contains the urls of the floor plans of the building, which is displayed based on Dialogflow intent and entity detected.
"""
class MapUrls:
    def display_map_url(place):
        html_floor_plan_toilets = 'https://prnt.sc/nuUPRWC1WvY4'
        html_floor_plan_lifta = 'https://prnt.sc/axr2bJPgoDGC'
        html_floor_plan_liftb = 'https://prnt.sc/sFhlk-MbpjaC'
        html_floor_plan_bg = 'https://prnt.sc/vOEF096O6plq'
        html_floor_plan_cafetaria = 'https://prnt.sc/3vprHF62F7k1'
        html_floor_plan_theatre1 = 'https://prnt.sc/pnd8pomqAACq'
        html_floor_plan_theatre2 = 'https://prnt.sc/c1glmajAlA-l'
        html_floor_plan_floor2_theatre3 = 'https://prnt.sc/bJgt0EXOB37J'
        html_floor_plan_floor2_theatre45 = 'https://prnt.sc/aNnAZKfoKP7h'
        html_floor_plan_secondfloor = 'https://prnt.sc/pishhugsMgQA'
        html_floor_plan_campus = 'https://prnt.sc/Bh_4tIcqYDL4'

        if place == "Toilet":
            return html_floor_plan_toilets
        elif place in ["Lift Wing A", "Computer science", "Mathematics", "Environmental study", "SAIL AI LAB", "Robot Lab", "Marketing", "UCGB", "VU Education Lab", "Beta Common room", "Rialto/Griffoen Office"]:
            return html_floor_plan_lifta
        elif place in ["Nursing", "Lift Wing B", "Cinema", "lecture", "Theater 6", "Theater 7", "Theater 8", "Theater 9", "Network Institute Tech Labs", "Physical Computing Education Lab", "Hardware/Multipurpose Lab"]:
            return html_floor_plan_liftb
        elif place in ["NU Building", "Lift", "Study", "parking", "room", "Firstaid"]:
            return html_floor_plan_bg
        elif place == "Cafeteria":
            return html_floor_plan_cafetaria
        elif place == "Theater 1":
            return html_floor_plan_theatre1
        elif place == "Theater 2":
            return html_floor_plan_theatre2
        elif place == "Theater 3":
            return html_floor_plan_floor2_theatre3
        elif place in ["Theater 4", "Theater 5"]:
            return html_floor_plan_floor2_theatre45
        elif place == "Meeting rooms":
            return html_floor_plan_secondfloor
        else:
            return html_floor_plan_campus