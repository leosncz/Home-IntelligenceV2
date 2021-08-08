# Author: @leosncz
# This file can be edited

# Those words are meant to separate orders like turn on the lights in my room AND turn off the light in the livin room.
# In this case, AND is a separator word.
separator_words = ['and','then','et','puis'] # Here I put only english & french separator words, up to you to add in your language

# This part is self-explanatory
orders = {"allume": {"salon": "urlsalonallume", "cuisine": "urlcuisineallume", "entre": "url"},
	"eteint": {"salon": "urlsaloneteint", "cuisine": "urlcuisineeteint", "entre": "url"},
	"ouvre": {"portail": "url"},
	"ferme": {"portail": "url"}
	}

# Interval in second when the software should update its camera understanding
cam_interval = 5
