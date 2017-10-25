# Aula 01

Variaveis
--------------

As variavéis (como em matemática) recebem valores, n, os quais
podem ser alterados e o são, em alguns casos de acordo com tipo
que é definida (uma string - cadeia de caracteres - numero
reais, ou inteiros) de acordo com a linguagem de programação.








Operações Aritméticas
------------------------
Têm-se usualmente como ocorrido em matemática incluindo a ordem com a
qual as operações são executadas, operadores para: soma, subtração, divisão
potência, e outros desde que suportados pela linguagem ou definidos na mesma
através de 'funções' (será visto mais a frente)




Operações Lógicas & Tabela Verdade
------------------------------------

Os operadores lógico básicos são E, OU, NÃO (outros surgem
da combinação dos mesmo como NAND e XOR).

<table style="margin: 15px; padding: 5px;border: 2px; background-color: beige;">
<tr><th>x</th><th>y</th><th>x E y</th><th>x OU y</th><th>NOT y</th> <th>x NAND y</th> <th>x XOR y</th></tr>
<tbody>
	<tr> <td>1</td> <td>1</td> <td>1</td> <td>1</td> <td>0</td> <td>0</td> <td>0</td> </tr>
	<tr> <td>1</td> <td>0</td> <td>0</td> <td>1</td> <td>1</td> <td>1</td> <td>1</td> </tr>
	<tr> <td>0</td> <td>1</td> <td>0</td> <td>1</td> <td>-</td> <td>1</td> <td>1</td> </tr>
	<tr> <td>0</td> <td>0</td> <td>0</td> <td>0</td> <td>-</td> <td>1</td> <td>0</td> </tr>
<tbody>
	
</table>
<br><br>

(Portas XOR, NAND, NOR em https://pt.wikipedia.org/wiki/Porta_XOR e https://pt.wikipedia.org/wiki/Tabela_verdade 
para mais detalhes.)

Essas tabelas e conectivos (operadores) lógicos serão usados <br>
no momento da construção de condições a serem testadas <br>
como verdadeiras ou falsas quando a condição <br>
é satisfeita (no caso 'verdadeiro') ou não <br>
é satisfeita (no caso falso). <br>
<br>
Exemplo: Trocar uma lâmpada.
<br>
Condição: <b>Se</b> a lampada esta queimada <b> ou </b> venceu seu prazo de validade <br>
Resultado: <i>'Eu troco a lampada.'</i> <br>
Note o uso do <i>se</i> e do <i>ou</i> (o OU como na tabela acima, <b>x OU y</b>)


IO - Entrada e Saida de Dados (E/S)
------------------------------------

De inicio abordaremos a entrada de dados via terminal (console, prompt), ou
seja, modo texto. Em cada linguagem a uma 'palavra reservada especifica' (função)
responsável tanto pela entrada de dados, lendo o que é digitado pelo usuários;
como para a saida de dados, exibindo no terminal o que fôra especificado
pelo programador como mensagem a ser exibida.


<br><br>
<i>Veja codigo [aula01.py](https://github.com/wsricardo/mcestudos/blob/master/aulas/aula1/aula01.py) </i>
<br>
Prossiga para Aula 02 ...
