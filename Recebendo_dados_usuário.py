"""
Recebendo dados do usuário
"""

# Entrada de dados
print("Qual o seu nome ? ")
nome = input()

print("Seja bem-vindo(a) %s" % nome)

print("Qual sua idade ? ")
idade = input()

# Processamento

# Saída
print('%s tem %s anos' % (nome, idade))

# Outro exemplo, mas só que mais moderno para essa versão atual (versões 3.x)

print('Seja bem-vindo(a) {0}' .format(nome))

print("Qual sua idade ? ")
idade = input()