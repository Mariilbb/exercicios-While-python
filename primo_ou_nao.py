# o usuario deve escolher um numero e o programa dizer se ele é primo ou não

num = int(input("digite um numero: "))
i = 2 # começa em 2 para sabermos se o numero é par, se for, ele não é primo

while i < num: # o i deve ser menor que o num pq n se pode dividir um numero menor por um divisor maior se estamos trabalhando com inteiros
    if num % i == 0: # se o numero digitado for dividido por 2 e restar 0, ele não é primo
        print(f"{num} não é primo")
        break
    i += 1
else:
    print(f"{num} é primo")