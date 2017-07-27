import urllib.request
preço = 99.99 #algum valor maior
while preço >= 4.74:
    pagina = urllib.request.urlopen(
    'http://beans.itcarlow.ie/prices-loyalty.html') 
    texto = pagina.read().decode('utf8') 
    onde = texto.find('>$')
    início = onde + 2
    fim = início + 4
    preço = float(texto[início:fim])
print ('Comprar! Preço: %.2f' %preço)

