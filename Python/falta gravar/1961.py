pulo, qtd = input().split()

pulo = int(pulo)
qtd = int(qtd)
torres = []

torres = list(map(int, input().split(' ')))

tam = len(torres)-2
verifica = 1
l = 0
while l <= tam:
    if torres[l+1] > torres[l]:
        if (torres[l]+pulo) < torres[l+1]:
            verifica = 0
    else:
        if (torres[l+1]+pulo) < torres[l]:
            verifica = 0

    l+=1


if verifica == 1:
    print('YOU WIN')
else:
    print('GAME OVER')
