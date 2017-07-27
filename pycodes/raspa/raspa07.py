from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")
print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).
          parent.previous_sibling.get_text())
#<tr>
# <td>
# <td>
# <td>
#    "$15.00" (4)
# <td> (2)
#    <img src="../img/gifts/img1.jpg"> (1)
#(1) seleciono a imagem
#(2) seleciono o parent (td que envolve a imagem)
#(3) com previous_sibling seleciono a tag que contêm o preço
#(4) mostro o texto dentro da tag
