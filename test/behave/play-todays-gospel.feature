Feature: play-todays-gospel
  Scenario: play today's gospel in English
    Given an english speaking user
     When the user says "Play today's Gospel"
     Then "todays-gospel-skill" should reply with dialog from "gospel.todays.dialog"
