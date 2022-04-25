"""
Tipo Boolean

Retornar somente valores verdadeiro ou false, True ou False
OBS: Sempre com a primeira letra maiuscula, True, False

"""

tipoBooleano = True
print(f' Valor é = {tipoBooleano}, e o tipo dessa variável é = ', type(tipoBooleano))

"""
Operações básicas
"""
# Negação (not)
# Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso, ser o valor for falso o resultado é verdadeiro
# Veja que o valor da variavel tipoBooleano é True e quando usamos a negação ele imprime False, veja o print abaixo.
print(not tipoBooleano)

# Ou (or)
# É uma operação binária precisa de dois valores. se um dos valores for verdadeiro o resultado será verdadeiro.
ativo = True
logado = False
print(ativo or logado)

# E (And)
# É operação binária precisa de dois valores, retorna verdadeiro se os dois valores for verdadeiros
# True and True o resultado será verdade