#!/usr/bin/python3
#-*- coding: utf8 -*-

# Código de exemplo sobre Orientação a objeto com a linguagem Python.
# Primeiro a classe geral serVivo
# Depois a classe 'Humano' que deriva da classe 'Animal' herdando seus metodos e atributos.
# Neste caso a class (classe) Humano herdar Animal significa que os atributos também 
# parte do ser humano.
# Exemplo: Animal com atributo 'idade' também faz parte de Humano, por exemplo, um menino
# chamado 'Pedro' a variavel 'pessoa' é um objeto, ou seja, uma instancia criada da classe Humano
# Classes servem para definir "moldes" que servem como forma de modelar outros objetos
# que possuem semelhanças (atributos, ações que podem fazer/funções).
# www.python.org/docs Seção OO (Orientação a Objeto, POO).
class serVivo(object):
	def __init__(self, **kwargs):
		self.kwargs = kwargs
# Classe animal
class Animal(object):
	def __init__(self, *args):
		self.args = args
	def show(self,*kargs):
		print(self.args)
# Classe 'Humano' herdando a classe Animal.
class Humano(Animal):
	def __init__(self,  nome, idade):
		anima.__init__(self, nome, idade)
		self.nome = nome
		self.idade = idade
 
pessoa = humano('Pedro', '35')
pessoa.show()
# Output: ('Pedro', '35')
pessoa.args
# Conteudo no atributo 'args' herdado da class 'Animal' : ('Pedro', '35')
