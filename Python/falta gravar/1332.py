n = int(input())

for i in range(n):
    numero = input()

    cont1 = 0
    cont2 = 0
    res = 0


    if len(numero) == 5:
        res = 3
    else:
        if 'o' in numero:
            cont1+=1
            cont2+=1
        if 'w' in numero:
            cont2+=1
        if 't' in numero:
            cont2+=1
        if 'n' in numero:
            cont1+=1
        if 'e' in numero:
            cont1+=1
        if numero[2] == 'e':
            cont1+=1
        if numero[0] == 't':
            cont2+=1
        if numero[0] == 'o':
            cont1+=1
        if numero[1] == 'w' and numero[2] == 'o':
            cont2+=1
    if res == 3:
        print(3)
    else:
        if cont1 > cont2:
            print(1)
        else:
            print(2)

