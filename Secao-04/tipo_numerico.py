"""

Tipo numérico

Operações
"""

num = int(5)
print(num)

soma = int(10 + 2)
print(soma)

""" Veja que nesse formato imprime com casa decimal, flutuante. para imprimir inteiro informe o tipo int ou use //"""
divisao = ( 5 / 2)
divisao1 = int(5 / 2)
divisao2 = (5 // 2)
print(f'Decimal - {divisao}')
print(f'Inteiro -  {divisao1}')
print(f'Inteiro usando // - {divisao2}')

""" Para saber se o numero é par ou ímpar use módulo % , se o resto for 0(zero) o número é par se for 1 o número é ímpar """
resto = int(5 % 2)
print(f' O resto é: {resto}')

""" Para fazer um número elevado usa **, ex: 2 elevado a 8 """
elevado = int(2 ** 8)
print(f'2 elevado a 8 é: {elevado}')

""" Melhorando a forma de visualizar numeros para nós humanos, 1 milhão - 1000000 é pouco dificil de ver quando nesse formato então
podemos escrever nesse formato 1_000_000 """
""" declaramos na variavel assim, 1_000_000 mas veja como o python imprime """
umMilhao = int(1_000_000)
print(f'1 milhão = {umMilhao}')