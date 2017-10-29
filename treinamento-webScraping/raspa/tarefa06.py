import requests
from bs4 import BeautifulSoup as bs

prefix = "https://www.cinemark.com.br"
url_pagina = prefix + "/manaus/filmes/em-cartaz?pagina="
for npagina in (1, 2):    
    p = requests.get(url_pagina+str(npagina))
    s = bs(p.content, "html.parser")
    for filme in s.findAll('a', {'class':'movie-image'}):                     
        print (filme['title'][6:])
        print (prefix + filme['href'])
        
        
