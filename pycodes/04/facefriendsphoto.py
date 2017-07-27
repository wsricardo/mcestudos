#Sorry, in April 30, 2015, with Facebook 2.0 API update only friends that use the app will be show
import urllib.request
import json
from pprint import pprint

def save_image(friend):
  size = '/picture?width=200&height=200'
  url = 'https://graph.facebook.com/'+ friend['id'] + size
  image = urllib.request.urlopen(url).read()
  f = open(friend['name'] + '.jpg', 'wb')
  f.write(image)
  f.close()
  print (friend['name'] + '.jpg impresso')
#get the token https://developers.facebook.com/tools/explorer
token = 'EAACEdEose0cBAICsZBYhU7Jx6Yu4ZC1s9ZCgDV9CP1EvdjZCEeobufbmAer8PZBrJ5CFjIcXVEkZAbo2ZBoM8P8zzVq75qL5cHeIUoPEOyZARzEzvKPLyK0jZBJDT8z2Ih7kwyd50ugKyEZCopiKxuKae9lMHGQnFTYdV9aDOXmkyRZCEKAPgxfVN4zv91JnCAFP0AZD'
url = 'https://graph.facebook.com/me/friends?access_token='+token
resp = urllib.request.urlopen(url).read()
data = json.loads(resp.decode('utf-8'))

pprint(data)
for friend in data['data']:
  save_image(friend)

