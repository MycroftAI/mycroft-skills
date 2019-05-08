import datetime
from adapt.intent import IntentBuilder
from mycroft import intent_handler
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'viljanen'

LOGGER = getLogger(__name__)


class LectureSkill(MycroftSkill):



    def __init__(self):
        super(LectureSkill, self).__init__(name="LectureSkill")



    @intent_handler(IntentBuilder("LectureIntent").require("LectureKeyword").require("SubjectKeyword"))



    def handle_lecture_intent(self, message):

        f = open("/opt/mycroft/skills/lecture-subjects-skill/dates.txt", "r")     #open textfile
        dateFound = False
        lectureNumber = 0
        line = f.readline()
        if line[0] == "*":
            self.speak_dialog("default")
            dateFound = True
        while(line and not dateFound):                 #while right date hasn't been found and there is lines in the textfile, the program will read new lines from textfile
            lectureNumber += 1         #for each line the lectureNumber will go up
            y = int(line[0:4])         #yyyy
            m = int(line[4:6])         #mm
            d = int(line[6:8])       #dd
            date = datetime.date(y, m, d)
            if datetime.date.today() == date:    #check if date is today, speak accordingly
                self.speak_dialog("lecture" + str(lectureNumber))
                dateFound = True
            line = f.readline()

        if not dateFound:       #"no lecture today" if no date is found
            self.speak_dialog("nolecture")



        f.close()                      #close textfile



    def stop(self):
        pass




def create_skill():
    return LectureSkill()
