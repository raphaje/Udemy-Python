"""
PEP 8 - Python Enhancement Proposal
São proposta de melhorias para o python

The Zen of Python
Digitar no console, import this

A ideia PEP8 é que possamos escrever códigos Python de forma Phytônica que é um cógido seguindo padrão.

[1] - Utilize Camel Case para nomes de classes.
Ex:

class Calculadora:
ou
calss CalculadoraCientifica:


[2] - Utilize nomes em minúsculo, separados por underline para funções e variáveis
Ex:

Função:
def soma():
    pass
ou
def soma_dois()
    pass

Variável
numero = 4
ou
numero_impar = 3


[3] - Utilize quatro espaços para identação!  <-- Importante
Ex:
if 'a' in 'banana'
    print('tem')

Se não houver quatro espaço no print() o código não roda, fica atento as mensagem do IDE ele informa sobre identação.
OBS: Não use o Tab

[4] - Linhas em branco
    - Separar funções e definições de classes com duas linhas em branco.
    - Métodos dentro de classe devem ser separados com uma única linha em branco.

[5] - Imports
    - Imports devem ser feito sempre em linhas separadas.
Ex correto:
import sys
import os

Ex errado:
import sys, os

- Não há problema em utilizar o formato:
    from types import StringType, ListType
- Nesse formato estamos importando somente as classes StringType e ListType do pacote types.

No primeiro exemplo importados o pacote inteiro para o projeto.

OBS: Se for importar muitos itens do mesmo pacote recomenda-se usar o formato abaixo,
     sempre lembrando dos quatro espaços.

from types (
    StringTypes,
    ListTypes,
    SetType,
)

[6] - Espaços em expressões e instruções.
    # Não faça dessa forma.
funcao( algo[ 1 ], { outro: 2 } )

    # Forma correta
funcao(algo[1], {outro: 2})


[7] - Sempre termine uma instrução com uma linha em branco.
"""

if 'a' in 'banana':
    print('tem')
