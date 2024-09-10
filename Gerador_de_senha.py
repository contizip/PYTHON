import random
import string

def gerar_senha(comprimento, incluir_maiusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_simbolos=True):
    caracteres = ""
    
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation
    
    if not caracteres:
        raise ValueError("Você deve selecionar pelo menos um tipo de caractere.")
    
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

# Entrada do usuário
comprimento = int(input("Digite o comprimento desejado para a senha: "))
incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
incluir_minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
incluir_numeros = input("Incluir números? (s/n): ").lower() == 's'
incluir_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'

# Gerar a senha
senha_gerada = gerar_senha(comprimento, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_simbolos)

# Exibir a senha gerada
print(f"Sua senha gerada é: {senha_gerada}")