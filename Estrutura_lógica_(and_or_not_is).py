"""
Operadores unários:
    - not
Operadores binários:
    - and, or e is
"""
# Regras de funcionamento:

# Para o 'and', ambos os valores precisam ser True

ativo = True
logado = False

if ativo and logado:
    print('Bem-vindo usuário')
else:
    print('Acesse o link mandado no seu email por favor')

# Para o 'or', um ou outro valor precisar ser True

ativo = False
logado = False

if ativo and logado:
    print('Bem-vindo usuário')
else:
    print('Acesse o link mandado no seu email por favor')

# Para o 'not', o valor booleano  é invertido, ou seja,  se for True, vira False, se for False vira True.

if not ativo:
    print('Você precisa ativar a sua conta. Por favor verifique seu email.')
else:
    print('Bem-vindo usuário')

print(not True)

# Ativo é Falso ?

print(ativo is False)
