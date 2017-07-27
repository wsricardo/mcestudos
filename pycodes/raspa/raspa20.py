from twitter import *
import json
oauth=OAuth("14502701-Rv3I8pkWc5MqKSc8mgRwKTUCMjXRIZTQzoSvvJlIr",
            "aZdgnQKbsmyx8IDV7B3mkl34gckpJsL84Xy76wTgnUcyQ",
            "8SUXxeyCwWBk4US1dCDZuLgpc",
            "vmuEioQX5q1RCb40kclFqpslpLkaCaIJd2xpr6VJ14AMoivNbu")

twitter_stream = Twitter(auth=oauth)

results = twitter_stream.statuses.user_timeline(screen_name="fmasanori")
for status in results:
    print ("(%s) %s" % (status["created_at"],
                        status["text"].encode("ascii", "ignore")))
