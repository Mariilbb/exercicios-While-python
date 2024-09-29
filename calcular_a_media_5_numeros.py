#calcular a media de 5 numeros aleatorios digitados pelo usuário:

i = 1
soma = 0
n_num = 5 # é a quantidade de vezes que quero que o usuário digite um número

while i >= n_num:
    num = int(input("digite um número"))
    soma += num
    i += 1

media = soma/n_num
print(media)