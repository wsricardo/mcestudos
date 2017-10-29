from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")
images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})

url = 'http://www.pythonscraping.com/'
for image in images:
    img = image["src"]
    file = open(img[-8:], 'wb')
    print (img[-8:])
    figura = urlopen(url + img[2:]).read()
    file.write(figura)
    file.close()
    
