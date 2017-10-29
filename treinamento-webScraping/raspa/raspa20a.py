import tweepy

consumer_key = 	"8SUXxeyCwWBk4US1dCDZuLgpc"
consumer_secret = "vmuEioQX5q1RCb40kclFqpslpLkaCaIJd2xpr6VJ14AMoivNbu"

access_token = "14502701-Rv3I8pkWc5MqKSc8mgRwKTUCMjXRIZTQzoSvvJlIr"
access_token_secret = "aZdgnQKbsmyx8IDV7B3mkl34gckpJsL84Xy76wTgnUcyQ"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)
