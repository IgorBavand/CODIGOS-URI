while True:
    try:
        n,m = input().split()
        n = int(n)
        m = int(m)

        cont = 0

        for i in range(n,m+1):
            aux = str(i)
            aux = list(aux)
            tam = len(aux)
            aux2 = set(aux)
            tam2 = len(aux2)
            if tam == tam2:
                cont+=1

        print(cont) 

    except EOFError:
        break