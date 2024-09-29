# o usuário deve adivinhar um numero aleatorio de 1 a 100

import random #importa o random para ele dar numeros aleatorios

numero = random.randint(1,100) # os numeros que o random pode dar nesse caso são de 0 a 100
tentativas = 0

while True:
    tentativa = int(input("digite um número entre 1 e 100: "))
    tentativas += 1
    if tentativa == numero:
        print(f"parabens, você acertou em {tentativas} tentativas!")
        break
    elif tentativa < numero:
        print("tente um numero maior")
    else:
        print("tente um numero menor")
