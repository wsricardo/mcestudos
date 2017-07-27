#!/usr/bin/python3 -tt
#-*- coding: utf-8 -*-
# Facebook
# GUI - TK Básico e MVC 'Model View Control'
# 1. Iniciando Tkinter https://youtu.be/Wi_N0S48tOs
# 2. Iniciando MVC https://youtu.be/7gNCI7Dx0kU
# 'Python Para Zumbis'
# Aulas do Prof.: Fernando Masanori

from tkinter import*
import pygame.mixer

app = Tk()
app.title("Show de Calouros")
app.geometry('300x100+200+200')

sounds = pygame.mixer
sounds.init()
certos = IntVar()
certos.set(0)
errados = IntVar()
errados.set(0)

def espera_tocar(canal):
    while canal.get_busy():
        pass

def apertei_certo():
    #s = sounds.Sound('correct.wav')
    #espera_tocar(s.play())
    print('Apetei o botão "Certo!"')
    certos.set(certos.get() + 1)
    
def apertei_errado():
    #s = sounds.Sound('wrong.wav')
    #espera_tocar(s.play())
    print('Apetei o botão "Errado!"')      
    errados.set(errados.get() + 1)

lab = Label(app, text='Aperte os botões!', height = 3)
lab.pack()

lab1 = Label(app, textvariable = certos)
lab1.pack(side = 'left')
lab2 = Label(app, textvariable = errados)
lab2.pack(side = 'right')

b1 = Button(app, text = 'Certo!', width = 10,
            command = apertei_certo)
b1.pack(side = 'left', padx = 10, pady = 10)

b2 = Button(app, text = 'Errado!', width = 10,
            command = apertei_errado)
b2.pack(side = 'right', padx = 10, pady = 10)

app.mainloop()
