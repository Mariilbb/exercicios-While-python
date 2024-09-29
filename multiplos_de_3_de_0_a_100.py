# demonstrar quais são os multiplos de 3 de 0 a 100

i = 0 # começa em 0 pq o problema pede pra começar em 0 e ir até 100

while i <= 100: # como quero entre 0 e 100 coloca <=100
    if i % 3 == 0: # % significa resto de divisão, então se o i dividido por 3 restar 0, ele é multiplo de 3
        print(i)
    i += 1