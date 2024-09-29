i = 1
soma = 0
n_num = -1 # começa em menos um para que o while seja executado pelo menos uma vez

while n_num != 0:
    num = int(input("digite um numero:"))
    soma += num
    i += -1

media = soma/(i - 1) # a media é soma/(i-1) porque se o usuário digitar 0, o loop acaba, e se isso acontecer o i ja foi incrementado e tira 1 pra que o 0 n seja contado
print(media)