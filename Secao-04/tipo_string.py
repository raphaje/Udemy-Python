"""
Tipo String
Em Python, um dado é considerado String sempre que:
"""
# Estiver em àspas simples -> 'Uma String', '234', 'True', '34,1'
# Estiver em àspas duplas -> "Uma String", "234", "True", "34,1"
# Estiver em àspas simples triplas -> '''Uma String''', '''234''', '''True'''
# Estiver em àspas duplas triplas -> """Uma String""", """234""", """True"""

nome = 'Curso Python'
print(f'Valor da variável é = {nome}.', f'\nO tipo dessa variável é =', type(nome),f'\n')

nome = "Gina's Bar"
print(f'Valor da variável é = {nome}.', f'\nO tipo dessa variável é =', type(nome), f'\n')

## Com parágrafo
nome = 'Raphael \nJeronimo'
print(nome)

## Outra forma de parágrafo
nome = """Raphael
Jeronimo"""
print(f'{nome} \n')

## Caixa Alta(CAPS LOCK), O valor da variável está em minúsculo mas usando o upper imprimimos em maiúsculo
nome = 'Raphael Jeronimo'
print(f'{nome.upper()} \n')

## Caixa Baixa, O valor da variável está em maiúsculo mas usando o lower imprimimos tudo em minusculo
nome = 'RAPhael jerONIMO'
print(f'{nome.lower()} \n')

## Split, Pega cada uma das palavras e coloca em uma lista, OBS ISSO É IMPORTANTE PARA DESENVOLVER
## Quando usamos o split o Python faz o seguinte, cria um array no qual cada letra do nosso exemplo é uma string
## E cria um index para cada string dessa, ficando assim:
nome = 'Raphael Jeronimo Honorato'
print(f'Usando Split => {nome.split()} \n')

# String -> 'Raphael Jeronimo'
# É quebrado assim: Mais abaixo como seria o index, posição de cada string no array
# ['R', 'a', 'p', 'h', 'a', 'e', 'l', '', 'J', 'e', 'r', 'o', 'n', 'i', 'm', 'o']
# [ 0,   1,   2,   3,   4,   5,   6,   7,  8,   9,   10,  11,  12,  13,  14,  15 ]
# Vamos imprimir um intervalo informando as posições que queremos.
nome = 'Raphael Jeronimo'
print(f'Mostrando somente intervalo da posição 0 até 7 do nosso array => {nome[0:7]}') # Essa operação é chamado de slice de string
print(f'Mostrando somente intervalo da posição 8 até 16 do nosso array => {nome[8:16]} \n') # A posição 16 nem existe mas não esqueça que o python imprimi a posição anterior
# OBS: Veja que o python imprimi até a posição anterior que informamos,
# da posição 0:7 o python imprimi até o 6 que é a ultima string do nome Raphael
# se setasse até o 0:6 o python iria imprimir "Raphae".

"""
Invertendo as strings da lista
entendendo a nomemclatura
[::-1]
Primeiro ":" significa comece do primeiro elemento.
Segundo  ":" significa vá até o final do elemento.
O "-1" significa inverta
Veja Abaixo
"""
nome = 'Raphael Jeronimo'
print(f'Imprimindo invertido = {nome[::-1]} \n')

## Usando Split e imprimindo só a primeira lista
nome = 'Raphael Jeronimo'
print(f'Usando Split e imprimindo só a primeira lista')
print(f'{nome.split()[0]}\n')

## Usando replace, substituindo "a" pelo "i", veja que ele trocou todos.
nome = 'Raphael Jeronimo'
print(nome.replace('a', 'i'))
print('')

## Brincando com um palíndromo
nome = 'ana'
print(nome)
print(nome[::-1])
print('')

nome = 'socorram me subino onibus em marrocos'
print(nome)
print(nome[::-1])
