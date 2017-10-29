from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

#only siblings, except firt title row
for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)
#e se eu só tiver a tag do final? previous_siblings
#existem funções next_siblings e previous_sibling, retornam uma tag por vez
