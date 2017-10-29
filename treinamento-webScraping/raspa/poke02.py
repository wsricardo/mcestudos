import requests
import json
url = 'http://pokeapi.co/api/v2/type/3/'
res = requests.get(url)
res = json.loads(res.content.decode('utf-8'))
print ('Type:', res['name'])
print ('Half damage from: ', end = '')
for d in res['damage_relations']['half_damage_from']:
  print (d['name'], end = ' ')
print ('\nNo damage from: ', end = '')
for d in res['damage_relations']['no_damage_from']:
  print (d['name'], end = ' ')
print ('\nHalf damage to: ', end = '')
for d in res['damage_relations']['half_damage_to']:
  print (d['name'], end = ' ')
print ('\nDouble damage from: ', end = '')
for d in res['damage_relations']['double_damage_from']:
  print (d['name'], end = ' ')
print ('\nDouble damage to: ', end = '')
for d in res['damage_relations']['double_damage_to']:
  print (d['name'], end = ' ')
print ()
for pokemon in res['pokemon']:
  print (pokemon['pokemon']['name'])
