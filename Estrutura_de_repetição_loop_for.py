"""
Loop -> Estrutura de repetição.

For -> Uma dessas estruturas

Em C ou JAVA, fica mais ou menos assim:

for(int i = 0; i < 10; i++){
    //execução do loop
}

# Em python fica assim:

for item in interavel:
    //execução do loop

De forma geral, utilizamos loopes para iterar sobre sequências ou sobre valores
iteravéis.

# Exeplos iteráveis:
- Strings | nome = Guilherme Conti Teixeira
- Listas | lista = [1, 2, 3, 4, 5]
- Range | range[1, 10]
"""
nome = ('Guilherme')
lista = [1, 2, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista

# Exemplo de for 1 (iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)
"""
range(valor_inicial, valor_final)
OBS: O valor final não é inclusivo. Por exemplo: de um 1 a 10 ele só irá até do 1 ao 9
"""


# Exemplos de for 3 (iterando sobre um range)
for numero in range(1, 10):
    print(numero)


nome = 'Guilherme Conti Teixeira'
lista = [1, 3, 5, 7, 9]
numeros = range(1,10) # Temos que transformar em uma lista

for _, letra in enumerate(nome):
    print(letra)

"""
Quando não precisamos de uma valor e queremos descartar, utilizamos o _
"""

quantidade = int(input('Quantas vezes isso deve rodar ? '))
soma = 0

for n in range(1, quantidade+1):
    num = int(input(f'Informe o {n}/{quantidade} valor: '))
    soma = soma + num
print(f'A soma é `{soma}')

emoji = 'U0001F60D'

for num in range(1, 11):
    print('\001F60D * num)