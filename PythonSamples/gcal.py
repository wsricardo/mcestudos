#!/usr/bin/python3 -tt
#-*- coding: utf-8 -*-
# Doc Python Section about garbage collection
# Apagando instância da memória e liberando.
# https://docs.python.org/3.0/whatsnew/2.0.html#garbage-collection-of-cycles

class SomeClass(object):
	def __init__(self,*arg):
		self.arg = arg
	def show(self):
		print(self.arg)

		
instance = SomeClass([i for i in range(10)],
                     (1,2,3),
                     {'x':0.0,'y':0.0,'z':0.0})
instance.arg
instance.show()
del instance # Apaga da pilha a instancia da classe 'SomeClass'
print('End.')
