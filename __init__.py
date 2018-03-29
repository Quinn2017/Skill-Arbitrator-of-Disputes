# Copyright 2018 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.
#
# Visit https://docs.mycroft.ai/skill.creation for more detailed information
# on the structure of this skill and its containing folder, as well as
# instructions for designing your own skill based on this template.
#
#
# This skill is inspired from a combination of skills from Kathie Reid and Willem Ligtenberg
#
#
# Import statements: the list of outside modules you'll be using in your
# skills, whether from other files in mycroft-core or from external libraries

from os.path import dirname, join
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft.util import play_mp3
import random


# Logger: used for debug lines, like "LOGGER.debug(xyz)". These
# statements will show up in the command line when running Mycroft.
__author__ = 'Charles'

LOGGER = getLogger(__name__)

# The logic of each skill is contained within its own class, which inherits
# base methods from the MycroftSkill class with the syntax you can see below:
# "class ____Skill(MycroftSkill)"
class ArbitratorSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor.
    def __init__(self):
        super(ArbitratorSkill, self).__init__(name="ArbitratorSkill")

    # This method loads the files needed for the skill's functioning, and
    # creates and registers each intent that the skill uses.
    def initialize(self):
        self.load_data_files(dirname(__file__))

        decision_intent = IntentBuilder("DecisionIntent").\
            require("DecisionKeyword").build()
        self.register_intent(decision_intent, self.handle_decision_intent)

        consent_intent = IntentBuilder("ConsentIntent").\
            require("YesKeyword").build()
        self.register_intent(consent_intent, self.handle_consent_intent)

        termination_intent = IntentBuilder("TerminationIntent").\
            require("NoKeyword").build()
        self.register_intent(termination_intent, self.handle_termination_intent)

    # The "handle_xxxx_intent" functions define Mycroft's behavior when
    # each of the skill's intents is triggered: in this case, he simply
    # speaks a response. Note that the "speak_dialog" method doesn't
    # actually speak the text it's passed--instead, that text is the filename
    # of a file in the dialog folder, and Mycroft speaks its contents when
    # the method is called.

    def handle_consent_intent(self, message):
        self.speak_dialog("consent", expect_response=True)

    def handle_decision_intent(self, message):
        self.speak_dialog("arbitration")
        self.process.wait()
        self.speak_dialog("deliberating")
        self.process.wait()
        if bool(random.getrandbits(1)):
            self.process.wait()
            self.speak_dialog("decision.one")
        else:
            self.process.wait()
            self.speak_dialog("decision.two")

    def handle_termination_intent(self, message):
        self.speak_dialog("termination")
        self.stop()

    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution.

    def stop(self):
        pass

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.

def create_skill():
    return ArbitratorSkill()
