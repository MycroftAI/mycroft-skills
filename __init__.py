from mycroft import MycroftSkill, intent_file_handler


class TodaysGospel(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('gospel.todays.intent')
    def handle_gospel_todays(self, message):
        self.speak_dialog('gospel.todays')


def create_skill():
    return TodaysGospel()

