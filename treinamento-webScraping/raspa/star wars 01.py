
import requests
import json

url = 'http://swapi.co/api/people/'
for d in range(1, 10):
  d = '' if d == 1 else '?page='+str(d)
  res = requests.get(url+str(d))
  res = json.loads(res.content.decode('utf-8'))
  for actor in res['results']:
    print (actor['name'])
  
