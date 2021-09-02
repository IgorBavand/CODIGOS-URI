while True:
    m,n = input().split(' ')

    m = int(m)
    n = int(n)

    if m == 0 and n == 0:
        break

    soma = m+n
    soma = str(soma)

    soma = soma.replace('0','')
    print(soma)

