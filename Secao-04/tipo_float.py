""" Tipo Float
também conhecido como Real, decimal
OBS: O separador de casas decimais é ponto (.) e não virgula (,)
"""

# Forma Errado para ser um float mas essa forma gera uma tupla que veremos essa estrutura mais a frente.
valorErrado = 1, 44  # lembre-se da pep, sempre tem um espaço após uma virgula
print(f'Valor Errado = {valorErrado}')
print(type(valorErrado))  # O type mostra o tipo dessa variável que nesse caso é uma tupla e não um float

# Forma Correto
valorCorreto = 1.44
print(f'Valor Correto = {valorCorreto}')
print(type(valorCorreto))

# É possível fazer dupla atribuição, ou seja, declaro duas variaveis e atributo seus valores tudo separado por virgula
valor1, valor2 = 1, 44

print(f'Valor 1 = {valor1}')
print(f'Valor 2 = {valor2}')

# Verificando o tipo da variavel
print(f'valor1 é do tipo =>', type(valor1))
print(f'valor2 é do tipo =>', type(valor2))

# Convertendo float para inteiro
# OBS: Ao converter do float para inteiro perdemos a precisão, veja o resultado.
resultado = int(valorCorreto)
print(f'Resultado da conversão é = {resultado}')

# NÚMEROS COMPLEXOS
"""
Sempre que quisermos declarar um número devemos fazer da seguinte forma
numero junto com a letra J
ex: 5j
"""
numComplexo = 5j
print(f'O tipo da variavel numComplexo é = ', type(numComplexo))