from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    print(bsObj.h1.get_text())
    #todos os títulos estão debaixo h1 > span
    print(bsObj.find(id ="mw-content-text").findAll("p")[0].get_text())
    #todo corpo de texto está no "mw-content-text" > p
    
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #We have encountered a new page
                newPage = link.attrs['href']
                print("===================\n"+newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks("") 
