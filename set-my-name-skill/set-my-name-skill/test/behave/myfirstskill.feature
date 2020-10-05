Feature: mycroft-myfirstskill

  Scenario Outline: current myfirtstskill
    Given an english speaking user
     When the user says "<my first skill>"
     Then "mycroft-my-first-skill-skill" should reply with dialog from "skill.first.my.dialog"

  Examples: myfirstskill activate
	| my first skill |
	| my first skill |
	| my first |
	| first |
	| skill |



   

