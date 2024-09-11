"""
Tipo string

Em Python, um dado é considerado do tipo string sempre que etiver entre
apas simples, duplas, triplas ou duplas triplas.

nome = 'Guilherme Conti Teixeira'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'NVIDEA \né muito bom'
print(nome)
print(type(nome))

nome = 'Carros'
print(nome.upper())

nome = 'Carros'
print(nome.lower())
"""
nome = 'Guilherme na Roque'
print(nome[0:4]) # Esta operação se chama de slice de string

# Exemplo de execução

# ['Guilherme', 'na']
print(nome.split()[0])
