# codigo que imprima os n primeiros numeros de fibonacci

n = int(input("digite o numero da sequencia de fibonacci: "))
anterior = 0 # numero que antecede o inicio de fibonacci
atual = 1 # fibonacci começa com o numero 1
i = 1

while i <= n:
    print(atual) # o numero atual é 1, pois foi o que estabelecemos
    proximo = anterior + atual # padrão da sequencia de fibonacci, o proximo é sempre a soma do anterior com o atual
    anterior = atual # apos o passo anterior, o numero anterior atualiza para o numero que estava agora
    atual = proximo # e então o numero atual se torna o proximo
    i += 1