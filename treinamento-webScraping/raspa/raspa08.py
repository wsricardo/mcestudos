from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")
images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:
    print(image['src'])

#metacharacteres: . ^ $ * + ? { } [ ] \ | ( )
#n.o pode ser não, nao, nxo... inclusive n.o
#n[aã]o só pode ser nao ou não
#fala[r!]? opcional falar, fala!, fala
#[a-z]* pode ser a até z quantas vezes aparecer, zero inclusive
#6+0 60, 660, 6660, ... (tem que ter pelo menos uma vez)
#{1,3}	de 1 a 3 vezes
#{4} exatamente 4 vezes
#[^0-9] é qualquer coisa fora números negação (dentro dos colchetes)
#^[0-9] número no início
#[0-9]$ número no final
#\ neutraliza o metacharacter
#?! não contem ^((?![A-Z].)*$ não usar maiúsculas, símbolos ok
#b(a|e|o)d  começa com b, termina com d, no meio podemos ter a ou e ou o
#[A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|edu|net) email
#\d{5}-\d{3} cep
#[A-Z]{3}-\d{4} placa de carro no Brasil
