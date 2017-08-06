import re
import urllib
import requests

class wSoupCrawler:
	"""
		Web Simple  Crawler.

		Lista de Funções:
				findtag: parametro -> tagname, return -> posição da tag
				catchbodytag: 
					parametros: tagname, tag_class_div, tag_id_div, tag_class_css, tag_id_css
				
				Funções Privadas: starttag, endtag ("abre e frecha tag") retorna posição de abertura e fechamento da tag.

	"""
	def __init__(self, url, *args):
		self.url = url
		self.args = args
		self.content= ''		
		#print('Start')

	def urlGet(self):
		"""
			Retorna conteudo em formato string.
		"""
		self.content = requests.get(self.url)
		return self.content.text

	def urlname(self):
		return self.url		

	def findtag(self, tagname):
		pos = 0
		return pos
	

	def catchbodytag(self, tagname, tag_class_div=None, tag_id_div=None):
		content_body_tag = '' # Conteudo interno da tag. Sometente textos, sem as tags nternas.
		return content_body_tag


	# Metodos internos (privados)
	def _starttag(self):
	
		pass
	def _endtag(self):

		pass
