n = int(input())

for i in range(n):
    numeros = []
    impares = []
    x,y = input().split(' ')
    x = int(x)
    y = int(y)
    numeros.append(x)
    numeros.append(y)
    numeros = sorted(numeros)

    for l in range(numeros[0]+1,numeros[1]):
        if l%2 != 0:
            impares.append(l)

    print(sum(impares))