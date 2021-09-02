n = int(input())
for l in range(n):
    diamantes = input()

    diamantes = diamantes.replace('.', '')
    diamantes = diamantes.replace(',', '')

    contador = 0
    veri = True

    while veri:
        cont = diamantes.count('<>')
        if '<>' in diamantes:
            diamantes = diamantes.replace('<>', '')
            contador = contador+cont
        else:
            veri = False

    print(contador)
    
    