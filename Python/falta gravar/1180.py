n = int(input())
numeros = []

numeros = list(map(str, input().split(' ')))
menor = min(numeros)

print('Menor valor: {}'.format(menor))
print('Posicao: {}'.format(numeros.index(menor)))