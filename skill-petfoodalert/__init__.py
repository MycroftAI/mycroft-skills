# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler

class PetFoodAlert(MycroftSkill):
    @intent_handler(IntentBuilder("").require("Pet").optionally('FoodYES').optionally('FoodNO').optionally('FoodMODERATE').optionally('FoodIF'))
    def handle_intent(self, message):
            mealtimeNO = message.data.get('FoodNO')
            print(mealtimeNO)
            mealtimeMODERATE = message.data.get('FoodMODERATE')
            print(mealtimeMODERATE)
            mealtimeYES = message.data.get('FoodYES')
            print(mealtimeYES)
            mealtimeIF = message.data.get('FoodIF')
            print(mealtimeIF)
            if mealtimeYES:
                self.speak('Yes.')
            elif mealtimeNO and not (mealtimeYES or mealtimeMODERATE):
                self.speak('No.')
            elif mealtimeMODERATE:
                self.speak('Yes, but in moderate amounts.')
            elif mealtimeIF:
                self.speak('Yes, but only if prepared correctly.')
            else:
                self.speak('Not yet in the database.')

    def stop(self):
        pass

def create_skill():
    return PetFoodAlert()
