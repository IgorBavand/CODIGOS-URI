n = int(input())

pares = []
impares = []

for i in range(n):
    numero = int(input())
    if numero%2==0:
        pares.append(numero)
    else:
        impares.append(numero)

pares = sorted(pares)
impares = sorted(impares, reverse=True)

for i in range(len(pares)):
    print(pares[i])
for l in range(len(impares)):
    print(impares[l])
    

