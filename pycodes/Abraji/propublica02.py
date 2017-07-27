from urllib.request import Request, urlopen
import json

url = "https://api.propublica.org/campaign-finance/v1/2016/committees/leadership.json"

q = Request(url)
q.add_header('X-API-Key', 'n8QLPm4lNS2Mfak1bam5X7HlevBAOSoF9epQkX0m')
data = urlopen(q).read()
data = json.loads(data.decode('utf-8'))

for committee in data['results']:
  print (committee['name'])
  print (committee['city'])
  print (committee['sponsor_name'])
  print ()
  
  
