#vetor1 = list(map(int, input('Digite os valores do vetor 1 separados por espaço: ').split()))

n = int(input())

for i in range(n):
    fila = []
    fila_organizada = []
    cont = 0
    qtd_casos = int(input())

    #ISSO AQUI RECEBE N VALORES DA LISTA NA MESMA LINHA
    #LEMBRE PQ VAI PRECISAR DISSO ANIMAL
    fila = list(map(int, input().split(' ')))
    fila_organizada = sorted(fila, reverse=True)

    for l in range(len(fila)):
        if fila[l] == fila_organizada[l]:
            cont+=1
    
    print(cont)