import requests
from bs4 import BeautifulSoup

url = 'https://www.yellowpages.com/search?search_terms=coffe&geo_location_terms=Los+angeles'
for k in range(1, 102):
  r = requests.get(url+'&page='+str(k))
  print (url+'&page='+str(k))
  s = BeautifulSoup(r.content, 'html.parser')
  data = s.findAll("div",
                   {"class":"info"})

  for item in data: print (item.getText())
