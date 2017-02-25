from os.path import dirname, join

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
import requests
import json


class LisaSkill(MycroftSkill):
    def __init__(self):
        super(LisaSkill, self).__init__(name="LisaSkill")

    def initialize(self):
        self.load_vocab_files(join(dirname(__file__), 'vocab', 'en-us'))

        prefixes = ['lisa']
        #self.__register_prefixed_regex(prefixes, "(?P<Word001>\w+) (?P<Word002>\w+) (?P<Word003>\w+")
        #self.__register_prefixed_regex(prefixes, "(?P<Word>\w+)")
        self.__register_prefixed_regex(prefixes, "(?P<Word>.*)")

        intent = IntentBuilder("LisaIntent").require("LisaKeyword").require("Word").build()
        self.register_intent(intent, self.handle_intent)

    def __register_prefixed_regex(self, prefixes, suffix_regex):
        for prefix in prefixes:
            self.register_regex(prefix + ' ' + suffix_regex)

    def getAnswer(self,sentence):
        payload = { 'sentence' : sentence }
        js = requests.get("http://localhost:5001/lisa/api/v1.0/ask",params=payload)
        data = js.json()['answer']
        return str(data)

    def handle_intent(self, message):
	sentence = message.data.get("Word").lower()
	# DEBUG
	#print sentence
	resp = self.getAnswer(sentence)

	if isinstance(resp, basestring):
        	self.speak(resp)

    def stop(self):
        pass


def create_skill():
    return LisaSkill()
