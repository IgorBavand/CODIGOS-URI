n = int(input())
numeros = []

for i in range(n):
    entrada = int(input())
    numeros.append(entrada)

#[8, 10, 8, 260, 4, 10, 10]
aux = sorted(set(numeros))
#[4, 8, 10, 260]

for l in range(len(aux)):
    print('{} aparece {} vez(es)'.format(aux[l], numeros.count(aux[l])))