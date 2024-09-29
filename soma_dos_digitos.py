# o usuario deve digitar um numero e o programa deve calcular a soma dos digitos

num = int(input("digite um numero: "))
soma = 0

while num > 0:
    resto = num % 10 # pega o numero e divide ele por 10 pra sumir o ultimo digito dele
    soma += resto # adiciona o numero q foi retirado a soma
    num = num // 10 # atualiza o numero, agora sem o ultimo digito 

print(f"a soma é {soma}")