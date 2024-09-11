"""
Escopo de variáveis

Dois casos de escopo

1- Variáveis globais:
    - Variáveis globais são reconhecidas no programa todo.

2- Variáveis locais:
    - Variaveis locais são reconhecidas apenas no bloco onde foram declaradas.

# Para declarar variáveis em Python fazemos:

nome_da_variável = valor_da_variável

Python é uma linguagem de tipagem dinâmica. Isso significa que ao
declararmos ela, nós não colocamos o tipo de dados dela. Este tipo é inferido
ao atribuírmos o valor á mesma.

Exemplo em C:
int numero = 42;

Em Java:
int numero = 42;

Em Python podemos fazer a reatribuição numa boa, em outras linguagens não.
Nas outras, se declaramos o int, não podemos colocar mais nada que não seja int.

numero = 42 # Exemplo global
print(numero)
print(type(numero))

numero = 'Guilherme'
print(numero)
print(type(numero))
"""
numero = 42
numero = 0

if numero > 10:
    novo = numero + 10 # A variável 'novo' está declarada localmente dentro do bloco if

    print(novo)
