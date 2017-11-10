from adapt.intent import IntentBuilder
import datetime
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft.configuration import ConfigurationManager
from mycroft.util import (
    create_signal,
    check_for_signal
)
from mycroft.messagebus.message import Message

__author__ = 'reginaneon'
globdate = str(datetime.date.today())
config = ConfigurationManager.get()

LOGGER = getLogger(__name__)


class CPISkipWakeWordsControlSkill(MycroftSkill):
    """
    Class name: CPISkipWakeWordsControlSkill

    Purpose: Creates the "CaffeineWizSkill" skill, which works using
        Mycroft-core with NeonGeckoCom modifications, provides the user with
        the functionality to choose between continuous audio recording, which
        would not require wake words for Mycroft to work, and the "standard"
        mode, where the wake word "Hey Mycroft" is required.

        In addition, this skill allows the user to modify their audio and text
        recording permissions, which is essential for the "my coupons" skill
        and general user privacy. Skill works with wide variety of potential
        requests phrases.

    Note: This skill would not proceed without the clear confirmation of
        the command from the user by asking

        "Should I stop skipping wake words?"

        and expecting a positive answer.


    Supporting Files:
         skill-skip-wake-words-control/vocab/en-us/ConfirmNo.voc
         skill-skip-wake-words-control/vocab/en-us/ConfirmYes.voc
         skill-skip-wake-words-control/vocab/en-us/StartSkipping1.voc
         skill-skip-wake-words-control/vocab/en-us/Skipping2.voc
         skill-skip-wake-words-control/vocab/en-us/Skipping3.voc
         skill-skip-wake-words-control/vocab/en-us/StopSkipping1.voc

         skill-skip-wake-words-control/test/intent/CPIConfirmIntentNo.intent.json
         skill-skip-wake-words-control/test/intent/CPIConfirmIntentYes.intent.json
         skill-skip-wake-words-control/test/intent/CPISkipWakeWordsStart.intent.json
         skill-skip-wake-words-control/test/intent/CPISkipWakeWordsStop.intent.json
        """

    def __init__(self):
        # name the new class:
        super(CPISkipWakeWordsControlSkill, self)\
            .__init__(name="CPISkipWakeWordsControlSkill")

    def initialize(self):
        # name intent and build it:
        start_skipping = IntentBuilder("StartSkippingWakeWords") \
            .require("StartSkipping1") \
            .require("Skipping2") \
            .require("Skipping3") \
            .build()
        # register:
        self.register_intent(start_skipping, self.handle_start_skipping)

        stop_skipping = IntentBuilder("StopSkippingWakeWords") \
            .require("StopSkipping1") \
            .require("Skipping2") \
            .require("Skipping3") \
            .build()
        # register:
        self.register_intent(stop_skipping, self.handle_stop_skipping)

        self.confirm_yes = IntentBuilder("ConfirmYes") \
            .require("ConfirmYes") \
            .build()
        # register:
        self.register_intent(self.confirm_yes, self.handle_confirm_yes)

        self.confirm_no = IntentBuilder("ConfirmNo") \
            .require("ConfirmNo") \
            .build()
        # register:
        self.register_intent(self.confirm_no, self.handle_confirm_no)

        self.disable_intent('ConfirmYes')
        self.disable_intent('ConfirmNo')

    def handle_start_skipping(self, message):

        self.speak("Should I start skipping wake words?", True)
        self.enable_intent('ConfirmYes')
        self.enable_intent('ConfirmNo')

        create_signal('StartSkippingWW')
        create_signal('WaitingToConfirm')

    def handle_stop_skipping(self, message):

        self.speak("Should I stop skipping wake words?", True)

        self.enable_intent('ConfirmYes')
        self.enable_intent('ConfirmNo')

        create_signal('StopSkippingWW')
        create_signal('WaitingToConfirm')

    def handle_confirm_yes(self, message):

        if check_for_signal("StartSkippingWW", 0):
            create_signal('skip_wake_word')
            create_signal('restartedFromSkill')
            self.speak("o k. Starting to skip wake words.", False)
            # self.emitter.emit(Message('configuration.updated'))
            # self.emitter.emit(Message('recognizer_loop:reload'))
            self.emitter.emit(Message('recognizer_loop:restart'))

        elif check_for_signal("StopSkippingWW", 0):
            check_for_signal('skip_wake_word', 0)
            create_signal('restartedFromSkill')
            self.speak("o k. Stopping the skipping of wake words.", False)
            # self.emitter.emit(Message('configuration.updated'))
            # self.emitter.emit(Message('recognizer_loop:reload'))
            self.emitter.emit(Message('recognizer_loop:restart'))

        self.disable_intent('ConfirmYes')
        self.disable_intent('ConfirmNo')

    def handle_confirm_no(self, message):
        self.speak("O K. Not doing anything.", False)

        self.disable_intent('ConfirmYes')
        self.disable_intent('ConfirmNo')

    def stop(self):
        pass


def create_skill():
    return CPISkipWakeWordsControlSkill()
