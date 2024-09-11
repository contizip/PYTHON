"""
Tipo Booleano

A expressão vem da algebra booleana, criada por Gerge Boole

2 constantes, verdadeiro ou falso

True
False

Sempre devem ser escritos com a inicial maiúscula ou minúscula
"""

ativo = True

print(ativo)

"""
Operações básicas:
"""

# Navegação (not):
"""
Fazendo a negação, se o valor booleano for verdadeiro, o resultado será falso,
se for falso, o resultado será verdadeiro. Ou seja, sempre irá ser o contrário.
"""

print(not ativo)

logado = False
"""
Se o valor booleano for verdadeira, o resultado será falso e vise versa
"""

# Ou (or)
"""
É uma operação binário, ou seja, depende de dois valores, Ou um ou outro deve ser verdadeiro.

True or True -> False
True or False -> True
False or True -> True
False or False -> False
"""

print(ativo or logado)

# E (and)
"""
Depende de dois valores, ambos os valores precisam ser verdadeiros.

True and True -> True
True and False -> False
False and True -> False
False and False -> True
"""

