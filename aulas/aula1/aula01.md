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

<table style="margin: 10px; border: 2px;">
<tr><th>x</th><th>y</th><th>x E y</th><th>x OU y</th><th>NOT y</th> <th>x NAND y</th> <th>x XOR y</th></tr>

	<tr> <td>1</td> <td>1</td> <td>1</td> <td>1</td> <td>0</td> <td>0</td> <td>0</td> </tr>
	<tr> <td>1</td> <td>0</td> <td>0</td> <td>1</td> <td>1</td> <td>1</td> <td>1</td> </tr>
	<tr> <td>0</td> <td>1</td> <td>0</td> <td>1</td> <td>-</td> <td>1</td> <td>1</td> </tr>
	<tr> <td>0</td> <td>0</td> <td>0</td> <td>0</td> <td>-</td> <td>1</td> <td>0</td> </tr>
	
	
</table>
<br>
|x |	y	|x E y		|x OU y	|	NOT y|
	
|:---------------------------------------------:|
|1 |	1		|1			|1			|0
|1 |	0		|0			|1			|1
|0 |	1		|0			|1			|-
|0 |	0		|0			|0			|-



IO - Entrada e Saida de Dados (E/S)
------------------------------------

De inicio abordaremos a entrada de dados via terminal (console, prompt), ou
seja, modo texto. Em cada linguagem a uma 'palavra reservada especifica' (função)
responsável tanto pela entrada de dados, lendo o que é digitado pelo usuários;
como para a saida de dados, exibindo no terminal o que fôra especificado
pelo programador como mensagem a ser exibida.

