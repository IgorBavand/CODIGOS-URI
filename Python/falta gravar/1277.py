n = int(input())

for i in range(n):
    qtd = int(input())
    nomes = []
    freq = []
    presentes = []
    veri = []

    nomes = list(map(str, input().split()))
    freq = list(map(str, input().split()))


    for l in range(len(freq)):
        aux = str(freq[l])
        aux = aux.replace('M', '')
        aux = list(aux)
        total = len(aux)
        ps = aux.count('P')
        percent = ps*100/total
         
        if percent < 75:
            presentes.append(l)


    if len(presentes) >= 1:
        for k in range(len(presentes)-1):
            print("{} ".format(nomes[presentes[k]]), end='')

        print('{}'.format(nomes[presentes[len(presentes)-1]]))
    else:
        print('')
    


        