while True:
    n = int(input())
    suspeitos = []
    ordem = []
    segundo = 0

    if n == 0:
        break

    suspeitos = list(map(int, input().split(' ')))

    ordem = sorted(suspeitos)

    print(suspeitos.index(ordem[-2])+1)