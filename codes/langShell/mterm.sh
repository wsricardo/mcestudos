#!/bin/bash

# fg - cor da frente (texto)
# bg - background (cor de fundo
# fn e fa tamanho do terminal e fonte com seu tamanho de letra
# -maximized (ou maximize) - especifica o estado da janela (quando em ambiente gráfico) como maximizado.
# -fullscreen - como anterior mas especificando o terminal em tela cheia.
xterm -fg green -bg black -fn 7x13 -fa "Mono:size=13" -sb -maximize -title 'Vim' &

