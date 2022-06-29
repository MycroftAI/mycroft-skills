import os
from mycroft import MycroftSkill, intent_file_handler
import requests
from bs4 import BeautifulSoup
from mycroft.audio import wait_while_speaking, is_speaking
from mycroft.util import get_cache_directory
from mycroft.util import play_mp3
from urllib.parse import quote
import subprocess

class TodaysGospel(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.p = None

    @intent_file_handler('gospel.todays.intent')
    def handle_gospel_todays(self, message):
        self.speak_dialog('gospel.todays')
        url = requests.get('https://evangeli.net/gospel')
        htmltext = url.text
        sp = BeautifulSoup(htmltext)
        mp3 = sp.find(title='listen').get('href')
        stream = '{}/stream'.format(get_cache_directory('TodaysGospelSkill'))
        # (Re)create Fifo
        if os.path.exists(stream):
            os.remove(stream)
        os.mkfifo(stream)
        self.log.debug('Running curl {}'.format(mp3))
        args = ['curl', '-L', quote(mp3, safe=":/"), '-o', stream]
        self.curl = subprocess.Popen(args)
        if is_speaking():
            wait_while_speaking()
        play_mp3(stream)

def create_skill():
    return TodaysGospel()

