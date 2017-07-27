from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")
nameList = bsObj.findAll("span", {"class":"green"})

for name in nameList:
    print(name.get_text())

#ver o HTML, claramente delimitados span {"class":"green"}
#findAll(tags, attributes, recursive, text, limit, keywords)
#tags pode ser mais de uma .findAll({"h1", "h2", "h3", "h4", "h5"})
#attributes pode ser uma expressão regular
#recursive = False não entra nos diversos subníveis, padrão é True
#findAll(text="the prince") procura "the prince" nas tags
#limit permite pegar um número limitado de tags
#keyword permite selecionar tags com um atributo particular findAll(id="text")
#será visto no raspa04.py
#obs.: findAll(class_="green")
