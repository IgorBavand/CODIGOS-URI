while True:
    n,m = input().split(' ')
    n = int(n)
    m = int(m)

    if n == 0 and m == 0:
        break

    contn = 0
    contm = 0

    while n > 0:
        contn = contn + n%10
        n = n/10

    while m > 0:
        contm = contm + m%10
        m = m/10

    repeticaon = True
    repeticaom = True
    contn = int(contn)
    contm = int(contm)

    auxn = 0
    auxm = 0
    while repeticaon:
        auxn = auxn+contn%10
        contn = contn/10
        #print(int(auxn))
        if int(auxn) <= 9 and int(contn) <= 0:
            break
        if int(contn) <= 0 and int(auxn) > 9:
            contn = auxn
            auxn = 0

    
    while repeticaom:
        auxm = auxm+contm%10
        contm = contm/10
       
        if int(auxm) <= 9 and int(contm) <= 0:
            break
        if int(contm) <= 0 and int(auxm) > 9:
            contm = auxm
            auxm = 0
    
    if auxn > auxm:
        print('1')
    elif auxm > auxn:
        print('2')
    else:
        print('0')

        


    