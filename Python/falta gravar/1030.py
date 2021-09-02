nc = int(input())

for i in range(nc):
    n,k = input().split()
    n = int(n)
    k = int(k)
    lista = []
    for l in range(1,n+1):
        lista.append(l)

    eliminacoes = k-1
    aux = 0
    while aux < 5:
        lista.pop(eliminacoes)
        print('posicao {} elemento {}'.format(eliminacoes, lista[eliminacoes]))
       
        
        eliminacoes = eliminacoes+k
       # if eliminacoes==len(lista): eliminacoes-=1
        if eliminacoes >= len(lista):
            eliminacoes = eliminacoes - len(lista)-1
        aux+=1

    print(lista)