import requests
import json
#gender
url = 'http://pokeapi.co/api/v2/ability/4/'
res = requests.get(url)
res = json.loads(res.content.decode('utf-8'))
for pokemon in res['pokemon']:
  print (pokemon['pokemon']['name'])
print (res['effect_entries'][0]['short_effect'])
print (res['effect_entries'][0]['effect'].replace('\n\n', ''))
