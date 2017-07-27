import json
from urllib.request import urlopen

ipAddress = "50.78.253.58"
resp = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
respJson = json.loads(resp)
print (respJson["country_name"])
print (respJson["region_name"])
print (respJson["latitude"])
print (respJson["longitude"])
