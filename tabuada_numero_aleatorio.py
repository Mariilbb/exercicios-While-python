# o usuario deve dar um numero e o programa mostrar a tabuada do mesmo de 1 a 10

n = int(input("digite um numero: "))
i = 1 # i começa em 1 pq o primeiro multiplicador é 1

while i <= 10:
    resultado = n * i
    print(f"{n} x {i} = {resultado}")
    i += 1