# o programa gera um numero aleatorio de 1 a 100 e o usuario deve adivinhar em no maximo 5 tentativas
# ele também deve receber dicas se está proximo ou não do numero

import random #importou random pra dar numeros aleatorios

num = random.randint(1,100)
tentativas = 0

while tentativas < 5: # se as tentativas forem menores que o maximo, nesse caso 5, roda o while
    tentativa = int(input("adivinhe o numero: "))
    tentativas += 1
    if tentativa == num:
        print(f"parabens, voce acertou em {tentativas} tentativas")
        break

    if abs (tentativa - num) <= 10: # abs serve pra deixar o numero positivo
        print("esta quente", end = ' ') # coloca o end com o espaço vazio para que possa adicionar uma nova mensagem a esta linha, nesse caso dizendo se o usuario deve tentar um numero maior ou menor
    else:
        print("esta frio", end = ' ')

    if tentativa < num:
        print("tente um numero maior", end = ' ')
    else:
        print("tente um numero menor", end = ' ')
    print(f"restam {5 - tentativas} tentativas")

if tentativas >= 5:
    print(f"voce não acertou em 5 tentativas. o numero era {num}")