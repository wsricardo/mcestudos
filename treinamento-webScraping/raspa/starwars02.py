import requests
import json

url = 'http://swapi.co/api/planets/'
res = requests.get(url)
res = json.loads(res.content.decode('utf-8'))
for planet in res['results']:
  print (planet['name'], planet['climate'],
         planet['terrain'])
