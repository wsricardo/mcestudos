#-----------------------------------------------------------------------
# twitter-stream-format:
#  - ultra-real-time stream of twitter's public timeline.
#    does some fancy output formatting.
#-----------------------------------------------------------------------

from twitter import *
import re

search_term = "anitta"

#-----------------------------------------------------------------------
# import a load of external features, for text display and date handling
# you will need the termcolor module:
#
# pip install termcolor
#-----------------------------------------------------------------------
from time import strftime
from textwrap import fill
from email.utils import parsedate

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
auth = OAuth("14502701-Rv3I8pkWc5MqKSc8mgRwKTUCMjXRIZTQzoSvvJlIr",
            "aZdgnQKbsmyx8IDV7B3mkl34gckpJsL84Xy76wTgnUcyQ",
            "8SUXxeyCwWBk4US1dCDZuLgpc",
            "vmuEioQX5q1RCb40kclFqpslpLkaCaIJd2xpr6VJ14AMoivNbu")
stream = TwitterStream(auth = auth, secure = True)

#-----------------------------------------------------------------------
# iterate over tweets matching this filter text
#-----------------------------------------------------------------------
tweet_iter = stream.statuses.filter(track = search_term)

pattern = re.compile("%s" % search_term, re.IGNORECASE)

for tweet in tweet_iter:
	# turn the date string into a date object that python can handle
	timestamp = parsedate(tweet["created_at"])

	# now format this nicely into HH:MM:SS format
	timetext = strftime("%H:%M:%S", timestamp)

	print ("(%s) @%s" % (timetext, tweet["user"]["screen_name"]))
	print ("%s" % (tweet["text"]))
