import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlretrieve

prf = 'http://www.raveolution.com/music/techno/'
p = requests.get(prf)
s = bs(p.content, 'html.parser')
for music in s.find_all('li')[1:]:
    m = music.find('a')['href']
    name = music.string.strip()
    urlm = prf + m
    print (urlm, name)
    urlretrieve(urlm, name)
