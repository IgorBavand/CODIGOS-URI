while True:
    n = int(input())
    palavras = []
    tamanhos = []

    if n == 0:
        break

    for i in range(n):
        entrada = input()
        palavras.append(entrada)

    for k in range(n):
        tamanhos.append(len(palavras[k]))

    maior = max(palavras, key=len)
    

    for l in range(len(palavras)):
        espacos = max(tamanhos) - len(palavras[l])-1
        if len(palavras[l]) < len(maior):
            print(' '*espacos,palavras[l])
            
        else:
            print(palavras[l])
            

    

    print('')