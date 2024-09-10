"""
1- Este exemplo abaixo é chamado de Camel Case. Isso porque no Python, a "leitura correta" das classes é feita com a primeira letra maiúscula e a segunda também.
Veja o exemplo correto logo abaixo que fiz:
"""

class Calculadora:
    pass
class calculadoreaCientifica:
    pass

"""
2- Utilizar nomes em minúsculo sperados por underlinepara funções ou variáveis:
"""

def soma():
    pass

def soma_dois():
    pass

numero_par = 4

numero_impar = 5

"""
3 - Indentação para quatro espaços

exemplo errado abaixo:
"""
if 'a' in 'banana':
print ('tem')

# correto

if 'a' in 'banana':
    print ('tem')

# Obs: utilize sempre quatro espaços. Não é recomendado usar a tecla TAB porque a configuração pode mudar de máquina e para IDE.

"""
4 - Separar funções e definições com duas linhas em branco
"""

"""
5 - Import sempre devem ser feitos em linhas separadas
"""

# Exemplo incorreto

import sys, os

# Exemplo correto

import sys
import os

# Não há problemas em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomanda-se fazer:

from types import {
    StringType,
    ListType,
    SetType,
    Outro
}

""" 
imports devem ser colocados no topo do arquivo, logo depois de quaisquer
comentarios ou doc strigs, e antes de constantes e variáveis gobais
"""
# 6 - espaço em expressões e instruções

# Errado

funcao( algo [ 1 ],  { outro: 2 } )

# Certo:

funcao(algo[1], {outro: 2})
