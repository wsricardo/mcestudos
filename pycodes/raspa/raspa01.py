from urllib.request import urlopen
#trazer a página inteira
html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
print(html.read().decode('utf-8'))
