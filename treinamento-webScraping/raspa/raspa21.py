from twitter import Twitter, OAuth
import json
#Acces Token, Access Token Secret, Consumer Key, Consumer Secret
t = Twitter(auth = OAuth("14502701-Rv3I8pkWc5MqKSc8mgRwKTUCMjXRIZTQzoSvvJlIr",
            "aZdgnQKbsmyx8IDV7B3mkl34gckpJsL84Xy76wTgnUcyQ",
            "8SUXxeyCwWBk4US1dCDZuLgpc",
            "vmuEioQX5q1RCb40kclFqpslpLkaCaIJd2xpr6VJ14AMoivNbu"))

resp = t.search.tweets(q="anitta")
for x in resp['statuses']:
  print (x['text'].encode("ascii", "ignore"))
