from lxml import html
from lxml.cssselect import CSSSelector
import requests

page = requests.get('https://www.aprovaconcursos.com.br/questoes-de-concurso/questoes/pagina/1/quantidade-por-pagina/30')
tree = html.fromstring(page.text)

rows = tree.cssselect(".questao.row");


def getEnunciadoSelector(depricated):
	if depricated:
		return "div.enunciado.row > div:nth-child(2)"
	else:
		return  "div.enunciado.row > div"

def getEnunciado(enunciado):
	list = []
	items = enunciado[0].getchildren()
	for e in items:
		list.append(e.text_content())

	return list

def getRespostas(respostas):
	list = []
	items = respostas
	for r in items:

		if len(r.getchildren()) > 1:
			r = r.getchildren()[1]

		list.append(r.text_content()
					.strip()
					.replace("\t", "")
					.replace("\n", "")
					.replace("a)", "")
					.replace("b)", "")
					.replace("c)", "")
					.replace("d)", "")
					.replace("e)", "")
					.replace("f)", "")
					.replace("  ", ""))

	return list


for row in rows:
	prova = row.cssselect('div.barra-top-2.col-sm-12 > span:nth-child(1) > a')
	disciplina = row.cssselect('div.barra-top-2.col-sm-12 > span:nth-child(3) > a')
	assuntos = row.cssselect('div.barra-top-2.col-sm-12 > span:nth-child(4) > a')
	depricated = row.cssselect('div.enunciado.row > div:nth-child(1) > p > strong:nth-child(2)')
	depricated = False if not depricated else True
	enunciado = row.cssselect(getEnunciadoSelector(depricated))
	respostas = row.cssselect('div.alternativas.row > div > form > ul > li > label.lbl > span')

	print ("prova: ", prova[0].text_content())
	print ("disciplina: ", disciplina[0].text_content())
	print ("assuntos: ", assuntos[0].text_content())
	print ("depricated: ", depricated)
	print ("enunciado: ", getEnunciado(enunciado))
	print ("respostas: ", getRespostas(respostas))
	
