import urllib.request
pagina = urllib.request.urlopen(
    'http://beans.itcarlow.ie/prices-loyalty.html') 
texto = pagina.read().decode('utf8') 
onde = texto.find('>$')
início = onde + 2
fim = início + 4
preço = texto[início:fim]
if preço < 4.74:
    print ('Comprar pois está barato:', preço)
else:
    print ('Esperar')
