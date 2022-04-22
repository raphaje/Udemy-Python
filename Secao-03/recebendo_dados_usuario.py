"""
Recebendo dados do usuário
"""
# Entrada de dados
print("Qual seu nome ?")
nome = input()

## Exemplo print "antigo" python 2.x
print('Seja bem vindo(a) %s' % nome )

## Exemplo print "moderno" python 3.x
print('Seja bem vindo(a) {0}' .format(nome) )

# Exemplo de print mais atual python 3.7.X
print(f'Seja bem vindo(a) {nome}')

print("Qual sua idade ?")
idade = input()

# Processamento

# Saída de dados
## Exemplo print "antigo" python 2.x
print('%s tem %s anos' % (nome, idade))

## Exemplo print "moderno" python 3.x
print('{0} tem {1} anos' .format(nome, idade))

# Exemplo de print mais atual python 3.7.X
print(f'{nome} tem {idade} anos')

"""
 int(idade) => cast
 cast é conversão de um tipo de dado para outro.
"""
print(f'{nome} nasceu em {2022 - int(idade)}')



# Outra forma para entrada de dados com menos código e mais fácil
nome1 = input('Qual seu nome ?')
idade1 = input('Qual sua idade ?')
print(f'{nome1} tem {idade1} anos')
