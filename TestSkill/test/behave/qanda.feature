Feature: Test Query

  Scenario Outline: user asks who someone is
    Given an english speaking user
     When the user says "<who is a person>"
     Then mycroft reply should contain "<person>"

  Examples: who questions
    | who is a person | person |
    | who is george church | church |
    | who are the foo fighters | foo |

  @xfail
  Scenario Outline: who questions failing due to Wolfram API outage
    Given an english speaking user
     When the user says "<failing wolfram query>"
     Then mycroft resply should contain "<expected answer>"

  Examples: failing wolfram questions
    | failing wolfram query | expected answer |
    | who built the eiffel tower | sauvestre |
    | who wrote the book outliers | gladwell |
    | who discovered helium | janssen |
    | what is the melting point of aluminum | 660 |
    | when was alexander the great born | 356 |
    | when will the sun die | billion |


  Scenario Outline: user asks a what question
    Given an english speaking user
     When the user says "<what is a thing>"
     Then mycroft reply should contain "<thing>"

  Examples: what questions
    | what is a thing | thing |
    | what is metallurgy | metallurgy |

  Scenario Outline: user asks when something is
    Given an english speaking user
     When the user says "<when did this happen>"
     Then mycroft reply should contain "<time>"

  Examples: when questions
    | when did this happen | time |
    | when was the last ice age | after the Medieval Warm Period |

  @xfail
  Scenario Outline: user asks where something is - failing due to Wolfram API outage
   Given an english speaking user
    When the user says "<where is a place>"
    Then mycroft reply should contain "<place>"

  Examples: what questions
    | where is a place | place |
    | where is morocco | africa |
    | where is saturn | saturn |
    | where is the smithsonian | washington |

  @xfail
  Scenario Outline: user asks a how question - failing due to Wolfram API outage
    Given an english speaking user
     When the user says "<how is this a thing>"
     Then mycroft reply should contain "<the answer>"

  Examples: what questions
    | how is this a thing | the answer |
    | how tall is the eiffel tower | 1063 |
    | how far away is the moon | distance |
    | how far is it from vienna to berlin | vienna |

  @xfail
  Scenario Outline: user asks a question mycroft can't answer
    Given an english speaking user
     When the user says "<failing query>"
     Then mycroft resply should contain "<expected answer>"

  Examples: what questions
    | failing query | expected answer |
    | what is a timer | interval |
    | what is the drinking age in canada | 19 |
    | how hot is the sun | sun |
