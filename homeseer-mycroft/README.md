# <img src='https://rawgithub.com/FortAwesome/Font-Awesome/master/advanced-options/raw-svg/solid/home.svg ' card_color='#004069' width='50' height='50' style='vertical-align:bottom'/> HomeSeer-Mycroft
Connect to your HomeSeer hub and control your smart-home devices using Mycroft.

## About 
A port of the HomeSeer functionality from Alexa to Mycroft. Allows the user to interact with smart-objects using voice control. Currently allows devices to be turned on/off, change values/percentages, lock/unlock items, and get the current status of any device. 

## Examples 
* "Mycroft, turn on the first floor bathroom light."
* "Mycroft, unlock the kitchen door lock."
* "Mycroft, set the first floor kitchen outside lights to 50%."
* "Mycroft, turn off all the first floor lights."
* "Mycroft, get the status of the first floor kitchen door lock."
* "Mycroft, run the Turn All Lights Off event."

## Configuration
Add the block below to your `mycroft.conf` file:

```json
  "HomeSeerSkill" : {
	"url": "HomeSeer server local IP",
	"username" : "Your HomeSeer account username. Put 'null' if local.",
	"password": "Your HomeSeer account password. Put 'null' if local."
  }
```

Remember to put `null` for username and password if your HomeSeer is on the same LAN as your Mycroft.
Restart Mycroft for the changes to take effect.

## Credits 
Sawyer McLane (@samclane)

## Category
**IoT**

## Tags
#homeseer
#homeautomation
#automation
#hub
#iot
#lights
#lighting
#smartlight
#smarthome
#smartbulb
#smartlock

[submodule "homeseer-mycroft"]
    path = homeseer-mycroft-skill
    url = https://github.com/samclane/homeseer-mycroft.git