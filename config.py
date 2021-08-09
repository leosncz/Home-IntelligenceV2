# Author: @leosncz
# This file can be edited

# Those words are meant to separate orders like turn on the lights in my room AND turn off the light in the livin room.
# In this case, AND is a separator word.
separator_words = ['and','then','et','puis'] # Here I put only english & french separator words, up to you to add in your language

# This part is self-explanatory
orders = {"allume": {"salon": "http://192.168.1.23/core/api/jeeApi.php?apikey=Yw4JQI9iAYwBHxQhEb3L8vGmPnYLbkT0&type=cmd&id=47", "cuisine": "http://192.168.1.23/core/api/jeeApi.php?apikey=Yw4JQI9iAYwBHxQhEb3L8vGmPnYLbkT0&type=cmd&id=227", "entrée": "url"},
	"éteins": {"salon": "http://192.168.1.23/core/api/jeeApi.php?apikey=Yw4JQI9iAYwBHxQhEb3L8vGmPnYLbkT0&type=cmd&id=48", "cuisine": "http://192.168.1.23/core/api/jeeApi.php?apikey=Yw4JQI9iAYwBHxQhEb3L8vGmPnYLbkT0&type=cmd&id=228", "entrée": "url"},
	"éteint": {"salon": "http://192.168.1.23/core/api/jeeApi.php?apikey=Yw4JQI9iAYwBHxQhEb3L8vGmPnYLbkT0&type=cmd&id=48", "cuisine": "http://192.168.1.23/core/api/jeeApi.php?apikey=Yw4JQI9iAYwBHxQhEb3L8vGmPnYLbkT0&type=cmd&id=228", "entrée": "url"},
	"etant": {"salon": "http://192.168.1.23/core/api/jeeApi.php?apikey=Yw4JQI9iAYwBHxQhEb3L8vGmPnYLbkT0&type=cmd&id=48", "cuisine": "http://192.168.1.23/core/api/jeeApi.php?apikey=Yw4JQI9iAYwBHxQhEb3L8vGmPnYLbkT0&type=cmd&id=228", "entrée": "url"},
	"ouvre": {"portail": "url"},
	"ferme": {"portail": "url"}
	}

# Interval in second when the software should update its camera understanding
cam_interval = 5

# If you want the software to not using any webcam, set this value to 'YES' (it is by default)
override_cam = 'YES' #'NO'
