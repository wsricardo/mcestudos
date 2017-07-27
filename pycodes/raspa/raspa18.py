import requests
from bs4 import BeautifulSoup

url = 'https://www.yellowpages.com/search?search_terms=coffe&geo_location_terms=Los+angeles'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')
#links = soup.find_all('a')

#for link in links:
#  print ("<a href='%s'>%s</a>" %(link.get('href'), link.text))

data = soup.find_all("div",{"class":"info"})

for item in data:
  print (item.text)
