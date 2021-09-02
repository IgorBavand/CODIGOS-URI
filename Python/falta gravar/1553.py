while True:

    n,k = input().split()
    n=int(n)
    k=int(k)

    if n == 0 and k == 0: break

    perguntas = []
    separados = []

    perguntas = list(map(str, input().split(' ')))

    separados = sorted(set(perguntas))

    cont = 0

    for i in range(len(separados)):
        if perguntas.count(separados[i]) >= k:
            cont+=1

    print(cont)
            




