from urllib.request import Request, urlopen
import json

url = "https://api.propublica.org/campaign-finance/v1/2016/president/totals.json"

q = Request(url)
q.add_header('X-API-Key', 'n8QLPm4lNS2Mfak1bam5X7HlevBAOSoF9epQkX0m')
data = urlopen(q).read()
data = json.loads(data.decode('utf-8'))

for candidate in data['results']:
  print (candidate['name'])
  print (candidate['total_contributions'])
  print (candidate['cash_on_hand'])
  
