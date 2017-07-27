from urllib.request import Request, urlopen
import json

url = "https://api.propublica.org/campaign-finance/v1/2016/committees/C00553560/filings.json"

q = Request(url)
q.add_header('X-API-Key', 'n8QLPm4lNS2Mfak1bam5X7HlevBAOSoF9epQkX0m')
data = urlopen(q).read()
data = json.loads(data.decode('utf-8'))

for committee in data['results']:
  print (committee['report_title'])
  print (committee['cash_on_hand'])
  print (committee['receipts_total'])
  print ()
  
  
