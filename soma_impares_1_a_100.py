# calcular a soma dos numeros impares de 1 a 100

i = 1  # começa em 1 pq vai de 1 a 100
soma = 0

while i <= 100:
    if i % 2 != 0: # se o i dividido por 2 restar algo diferente de 0, ai entra em loop
        soma += i
    i += 1

print(soma)