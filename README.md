# Laboratório 4: Conjectura de Collatz

Quarto projeto para submissão em Python de MC102 (Algoritmos e Programação de Computadores), curso ministrado pela UNICAMP.

Dando continuidade aos projetos desenvolvidos nos laboratórios de MC102 (explicação no repositório ["IniciandoEmPython"](https://github.com/laratoledom/IniciandoEmPython/blob/main/README.md)), temos como proposta de desenvolvimento do código o seguinte problema:
_______________________________________________________________________________________________________________________________________________________________________
  "A Conjectura de Collatz, conhecida também por Problema 3x+1, foi proposta pelo matemático alemão Lothar Collatz em 1937 e permanece em aberto desde então. Seu enunciado é bastante simples e requer apenas um número inteiro positivo x como entrada para o problema. Dado um número inteiro positivo x, caso x seja par, divida-o por dois. Caso contrário, multiplique-o por três e some um. O número resultante de uma dessas operações será o novo valor de x. Repita esse processo até que o valor de x seja igual a 1.

De maneira mais formal, temos que:

<p align="center">
  <img src="https://media.discordapp.net/attachments/1004187806345740310/1004209114420891728/Imagem2.png" />
</p>

Por exemplo, suponha que x seja inicialmente igual a 11. O número 11 é ímpar, dessa forma o novo valor de x será (3*11) + 1 = 34. Repetindo o processo temos que o número 34 é par, logo o novo valor de x será 34/2 = 17. Repetindo esse processo chegaremos eventualmente no número 1, quando o processo acaba.
A imagem a seguir mostra a sequência gerada a partir do número 11 até chegar no número 1. Os números com fundo na cor azul correspondem aos ímpares gerados, enquanto os com fundo na cor vermelha representam os números pares. <br><br>

<p align="center">
  <img src="https://media.discordapp.net/attachments/1004187806345740310/1004209647797940285/Imagem3.png" />
</p>

<br>
Note que os valores na sequência podem aumentar ou diminuir dependendo da paridade de x. A princípio, podemos ter a impressão de que esse processo pode nunca terminar, com o número 1 nunca sendo alcançado. Entretanto, o processo descrito acima foi testado em uma imensa quantidade de números inteiros positivos e até hoje nenhum contraexemplo foi encontrado. Contudo, uma prova matemática de que esse processo funciona para qualquer número inteiro positivo também não foi apresentada ainda.

O objetivo dessa atividade prática consiste em criarmos um programa que gere a sequência de números descrita pela Conjectura de Collatz a partir de um número inteiro positivo x.

Como entrada, seu programa receberá um número inteiro positivo N. Em seguida, seu programa receberá N números inteiros positivos. Para cada um dos N números inteiros positivos, seu programa deverá gerar a sequência de números seguindo a descrição apresentada pela Conjectura de Collatz. 

Além disso, o programa deverá ser capaz de computar a quantidade de números pares e ímpares na sequência, bem como o maior número presente na mesma. Como saída, para cada um dos N números inteiros positivos, seu programa deverá imprimir essas informações no seguinte padrão:

- Valor inicial: <b>X</b>
- Numeros Pares: <b>PARES</b>
- Numeros Impares: <b>IMPARES</b>
- Maior Numero: <b>MAX</b>

<br>
Onde <b>X</b>, <b>PARES</b>, <b>IMPARES</b> e <b>MAX</b> representam respectivamente o valor inicial dado como entrada, a quantidade de números pares na sequência, a quantidade de números ímpares na sequência e o maior número da sequência."

_______________________________________________________________________________________________________________________________________________________________________
<b>Observações:</b>
O arquivo foi executado através do PyCharm e no arquivo "testes" podem ser encontrados alguns exemplos de teste que verificam o código.
