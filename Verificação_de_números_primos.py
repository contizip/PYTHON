def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numero =  int(input('Digite um número: '))
if is_prime(numero):
    print(f"{numero} é primo")
else:
    print(f"{numero} não é primo.")