# tabela de conversão de graus celsius para fahrenheit, indo de -10 até 100 celsius

celsius = -10 # começa em -10 pq é o menor numero que pediu pra usarmos na tabela

while celsius <= 100:
    fahrenheit = (celsius * 9/5) + 32 # os valores são os usados para conversão
    print(f"{celsius} °C = {fahrenheit} °F")
    celsius += 10 # a conversão vai indo de 10 em 10 graus, por isso soma 10 ao celsius

# outra maneira de fazer, usando nomenclaturas diferentes

i = -10

while i <= 100:
    f = (i * 9/5) + 32
    print(f"{i} °C = {f} °F")
    i += 10