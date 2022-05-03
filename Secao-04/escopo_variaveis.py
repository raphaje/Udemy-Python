"""
Escopo de variáveis

Escopo significa que é um espaço delimitado, alguma coisa fica dentro desse espaço, nem antes e nem depois
fica dentro.

1 - Variável global
    São variáveis que são reconhecidas, ou seja, visto em qualquer parte do programa

2 - Variável local
    São variáveis que são reconhecidas, ou seja, vistas somente naquele bloco onde foram declaradas.

Para declarar variável
nome_da_variaavel = valor_da_variavel

Python é uma linguagem de dipos dinâmico, no qual não precisamos declarar o tipo dessa
variável.

"""
# Exemplo de variável local, ou seja, visto em qualquer parte do programa
numero = 11
print(numero)
print(type(numero))

# Veja o dois ponto : isso significa um bloco, logo a variavel "novo" é uma
# variável local, só é visto dentre bloco.
if numero > 10:
    novo = numero + 10
    print(novo)
