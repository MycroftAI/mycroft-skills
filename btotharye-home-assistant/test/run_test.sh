#!/bin/bash
source $TRAVIS_BUILD_DIR/mycroft-core/.venv/bin/activate
$TRAVIS_BUILD_DIR/mycroft-core/.venv/bin/python /opt/mycroft/skills/mycroft-homeassistant.btotharye/skill_developers_testrunner.py
