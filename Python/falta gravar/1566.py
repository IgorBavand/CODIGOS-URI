n = int(input())

for i in range(n):
    alturas = []
    

    qtd_pessoas = int(input())
    alturas = list(map(int, input().split(' ')))

    alturas = sorted(alturas)

    for l in range(qtd_pessoas):
        print('{} '.format(alturas[l]), end='')