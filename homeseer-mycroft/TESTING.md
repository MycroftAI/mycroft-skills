##homeseer-mycroft

#####Template
* Platform
    * Which platform is the test being run on? (i.e. Picroft, Mark 1, Linux)
* Device Version
    * What Mycroft version is the device running? (i.e. 18.02)
* Who
    * Who is running the test?
* Datestamp
    * Time and date of test
* Language 
    * i.e. "English, Australian" so that we can identify any key language issues
    
    
#####How to Install  homeseer-mycroft
* Install via `msm install https://github.com/samclane/homeseer-mycroft.git`
* All requirements are found in the `requirements.txt` folder
    * Note: `python-Levenshtein` is included in order to speed-up `fuzzywuzzy`. It is not required but is very nice.
* Add the block below to your `mycroft.conf` file:

If you have HomeSeer:
```json
  "HomeSeerSkill" : {
    "url": "HomeSeer server local IP",
    "username" : "Your HomeSeer account username. Put 'null' if local.",
    "password": "Your HomeSeer account password. Put 'null' if local."
  }
```
Note: Remember to put `null` for username and password if your HomeSeer is on the same LAN as your Mycroft.  


If you don't have a HomeSeer system, you can use the public demo API:
```json
  "HomeSeerSkill" : {
    "url" : "https://connected2.homeseer.com",
    "username" : "demo@homeseer.com",
    "password" : "demo100"
  }
```

Restart Mycroft for the changes to take effect.

* homseer-mycroft uses Python `requests` to send/receive JSON messages with the HomeSeer server.

#####How to Test  homeseer-mycroft
To begin, you should have a sense of what devices are connected to the HomeSeer hub. You can do this in your browser, 
by going to "http://`url`/?user=`username`&pass=`password`&request=getstatus". Note, you only need to add the username
and password if you're connecting to a non-local HomeSeer server. 

This should return a status JSON message, which will return all info about the current state of the system. Under 
`"Devices"`, you can see the names and statuses of all the devices on the network. Here's an example from the demo 
server:

```json
{  
  "Name":"HomeSeer Devices",
  "Version":"1.0",
  "Devices":[  
    {  
      "ref":7,
      "name":"test",
      "location":"Timers",
      "location2":"Counters-Timers",
      "value":150520690.4273926,
      "status":"1742:03:18:09",
      "device_type_string":"Timer",
      "last_change":"\/Date(1535479238204)\/",
      "relationship":0,
      "hide_from_view":false,
      "associated_devices":[  

      ],
      "device_type":{  
        "Device_API":0,
        "Device_API_Description":"No API",
        "Device_Type":0,
        "Device_Type_Description":"Type 0",
        "Device_SubType":0,
        "Device_SubType_Description":""
      },
      "device_image":"",
      "UserNote":"",
      "UserAccess":"Any",
      "status_image":"/images/HomeSeer/status/timers.png",
      "voice_command":"",
      "misc":4608,
      "interface_name":""
    },
    {  
      "ref":9,
      "name":"Floor Lamp",
      "location":"Office",
      "location2":"First",
      "value":100,
      "status":"On",
      "device_type_string":"",
      "last_change":"\/Date(1535463008049)\/",
      "relationship":0,
      "hide_from_view":false,
      "associated_devices":[  

      ],
      "device_type":{  
        "Device_API":0,
        "Device_API_Description":"No API",
        "Device_Type":0,
        "Device_Type_Description":"Type 0",
        "Device_SubType":0,
        "Device_SubType_Description":""
      },
      "device_image":"",
      "UserNote":"",
      "UserAccess":"Any",
      "status_image":"/images/HomeSeer/status/on.gif",
      "voice_command":"",
      "misc":4864,
      "interface_name":""
    },
    {  
      "ref":8,
      "name":"Table Lamp",
      "location":"Office",
      "location2":"First",
      "value":100,
      "status":"On",
      "device_type_string":"",
      "last_change":"\/Date(1535458384312)\/",
      "relationship":0,
      "hide_from_view":false,
      "associated_devices":[  

      ],
      "device_type":{  
        "Device_API":0,
        "Device_API_Description":"No API",
        "Device_Type":0,
        "Device_Type_Description":"Type 0",
        "Device_SubType":0,
        "Device_SubType_Description":""
      },
      "device_image":"",
      "UserNote":"",
      "UserAccess":"Any",
      "status_image":"/images/HomeSeer/status/on.gif",
      "voice_command":"",
      "misc":4864,
      "interface_name":""
    }
  ]
}
```

Using this info, you can craft Utterances with a general idea of which device it should effect, and how it will do so.

Example Demo Tests:
* "Mycroft, turn on floor lamp."
    * Floor Lamp status set to "on"
* "Mycroft, turn off all the lamps."
    * Desk Lamp and Floor Lamp will be set to "off"
* "Mycroft, get the status of the floor lamp."
    * Should respond "The floor lamp is (off|on)"
* "Mycroft, run the Luz al atardecer event."
    * For some reason, the only event on the demo server is in Spanish. 
    
Here are some other sample phrases:
* "Mycroft, turn on the first floor bathroom light."
* "Mycroft, unlock the kitchen door lock."
* "Mycroft, set the first floor kitchen outside lights to 50%."
* "Mycroft, turn off all the first floor lights."
* "Mycroft, get the status of the first floor kitchen door lock."
* "Mycroft, run the Turn All Lights Off event."

If you run the cli-debug client, you can see every http request the skill makes. In the url, you can see the info and 
verify your command was correctly parsed. If something goes wrong, Mycroft will tell you "there was a problem with 
HomeSeer" followed by an error message. 


#####Feedback
Please use the [Github Issues page](https://github.com/samclane/homeseer-mycroft/issues) to report bugs, give feedback,
and suggest new features (if needed). 