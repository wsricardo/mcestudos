import wsoup
import sys
import os

url_name = sys.argv[1]
if __name__ == '__main__':
	cont = wsoup.wSoupCrawler(url_name) # Conteudo html da web em string.
	text = cont.urlGet()
	print(text)
