from urllib.request import urlopen
#trazer a página inteira
html = urlopen("http://beans.itcarlow.ie/prices.html")
print(html.read().decode('utf-8'))
