while True:
    try:
        n, m = input().split()
        m = list(m)
        cont = 0
        for i in range(len(m)):
            cont = cont + int(m[i])
        
        if cont%3==0:
            res = 'sim'
        else:
            res = 'nao'


        print('{} {}'.format(cont,res))

    except EOFError:
        break