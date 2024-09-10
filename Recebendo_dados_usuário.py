"""
Recebendo dados do usuário
"""

# Entrada de dados
# print("Qual o seu nome ? ")
# nome = input()

# print("Seja bem-vindo(a) %s" % nome)

# print("Qual sua idade ? ")
# idade = input()

# Processamento

# Saída
# print('%s tem %s anos' % (nome, idade))

# Outro exemplo, mas só que mais moderno para essa versão atual (versões 3.x)

# print('Seja bem-vindo(a) {0}' .format(nome))

# rint("Qual sua idade ? ")
# idade = input()

"""Guilherme Conti Teixeria - Faculdade UNIARARAS"""
import datetime

nome = input('Qual seu nome ?')

print(f'Seja bem-vindo(a) {nome}')

idade = input('Qual a sua idade ?')

print(f'{nome} tem {idade} anos')

ano_atual = datetime.datetime.now().year
ano_nascimento = ano_atual - int(idade)

print(f'{nome} nasceu em {ano_nascimento}')
