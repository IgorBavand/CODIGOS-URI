n = int(input())

for i in range(n):
    frase = input()
    frase = list(frase)
    tamanho = int(len(frase)/2)-1
    decod = []
    while tamanho >= 0:
        decod.append(frase[tamanho])
        tamanho-=1

    aux = len(frase)-1
    tamanho = len(decod)

    while aux >= tamanho:
        decod.append(frase[aux])
        aux-=1
   
    final = ''.join(decod)
    print(final)