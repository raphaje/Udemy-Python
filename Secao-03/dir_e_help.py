"""
Utilitários python para auxiliar na programação

dir --> Apresenta todos os atributos, funções e métodos disponíveis para determinado tipo de dados e variáveis.

dir(tipo de dados ou variavel)

help --> Apresenta a documetação de como utilizar os atributos, funções e métodos disponíveis para determinado tipo de
dados ou variáveis.

Usando o help, no console python
help(tipoDado/variavel.propriedade)

Metodo upper() retorna a string tudo em maiusculo
Metodo lower() retorna a string tudo em minusculo
Metodo title() retorna a string no qual somente a primeira letra é maiuscula
"""

nome = input("Qual seu nome: ")
print(nome.upper())
print(nome.lower())
print(nome.title())

# Verificando que quais funcoes, metodos ou atributos posso usar para esse tipo de dados "raphael"
print(dir('raphael'))
