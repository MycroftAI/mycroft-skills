# Home Assistant Skill for Mycroft

based off the original code from https://github.com/BongoEADGC6/mycroft-home-assistant, spun off my own version since they seem to be inactive.

This is a skill to add [Home Assistant](https://home-assistant.io) support to
[Mycroft](https://mycroft.ai). Currently is supports turning on and off several
entity types (`light`, `switch`, `scene` and `input_boolean`).

## Installation

Clone the repository into your `~/.mycroft/skills` directory. Then install the
dependencies inside your mycroft virtual environment:

If on picroft just skip the workon part and the directory will be /opt/mycroft/skills

```
cd ~/.mycroft/skills
git clone https://github.com/btotharye/mycroft-homeassistant HomeAssistantSkill
workon mycroft
cd HomeAssistantSkill
pip install -r requirements.txt
```



## Configuration

Add a block to your `~/.mycroft/mycroft.conf` file like this:

```
  "HomeAssistantSkill": {
    "host": "hass.mylan.net",
    "password": "mysupersecrethasspass",
    "ssl": true|false
  }
```

NOTE: SSL support is currently secure as it does verify the cert.

You will then need to restart mycroft.

## Usage

Say something like "Hey Mycroft, turn on living room lights". Currently available commands
are "turn on" and "turn off". Matching to Home Assistant entity names is done by scanning
the HA API and looking for the closest matching friendly name. The matching is fuzzy (thanks
to the `fuzzywuzzy` module) so it should find the right entity most of the time, even if Mycroft
didn't quite get what you said.

## Supported Phrases/Entities
 Phrases are what is, where is, when is.  So where is Paul, what is brian commute to work (Commute to work would be in friendly name)
 
 * Lights
 * Sensor Status
 

## TODO
 * New intent for scene activation, e.g. "Mycroft, activate scene..."
 * Script intents processing
 * New intent for opening/closing cover entities
 * New intent for locking/unlocking lock entities (with added security?)
 * New intent for thermostat values, raising, etc.
 * ...

## Contributing

All contributions welcome:

 * Fork
 * Write code
 * Submit merge request

## Licence

See [`LICENCE`](https://gitlab.com/robconnolly/mycroft-home-assistant/blob/master/LICENSE).

