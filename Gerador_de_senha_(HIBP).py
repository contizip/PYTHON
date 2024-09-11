import random
import string
import hashlib
import requests

# Função para gerar uma senha segura
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

# Função para verificar se a senha foi vazada
def verificar_senha_vazada(senha):
    # Gerar o hash SHA-1 da senha
    sha1_senha = hashlib.sha1(senha.encode('utf-8')).hexdigest().upper()
    
    # Pegar os primeiros 5 caracteres do hash
    prefixo = sha1_senha[:5]
    sufixo = sha1_senha[5:]
    
    # URL da API Have I Been Pwned (HIBP)
    url = f"https://api.pwnedpasswords.com/range/{prefixo}"
    
    # Fazer a requisição para a API
    resposta = requests.get(url)
    
    # Verificar se a requisição foi bem-sucedida
    if resposta.status_code != 200:
        raise RuntimeError(f"Erro na requisição à API: {resposta.status_code}")
    
    # Verificar se a senha está nos resultados
    hashes_vazados = resposta.text.splitlines()
    for linha in hashes_vazados:
        hash_sufixo, contagem = linha.split(':')
        if hash_sufixo == sufixo:
            return True, int(contagem)  # Senha foi vazada, retorna a contagem de vazamentos
    
    return False, 0  # Senha não foi encontrada nos vazamentos

# Função principal que gera a senha e verifica se ela foi vazada
def main():
    # Entrada do usuário
    comprimento = int(input("Digite o comprimento desejado para a senha: "))
    incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
    incluir_minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
    incluir_numeros = input("Incluir números? (s/n): ").lower() == 's'
    incluir_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'

    # Gerar a senha
    senha_gerada = gerar_senha(comprimento, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_simbolos)
    
    # Verificar se a senha foi vazada
    vazada, contagem = verificar_senha_vazada(senha_gerada)

    if vazada:
        print(f"A senha gerada foi vazada {contagem} vezes! Tente gerar outra senha.")
    else:
        print(f"Sua senha gerada é segura: {senha_gerada}")

    # Pausa para manter a janela aberta
    input("\nPressione Enter para sair...")

# Executar a função principal
if __name__ == "__main__":
    main()
