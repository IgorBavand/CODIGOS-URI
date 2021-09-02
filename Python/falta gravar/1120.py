while True:
    d,n = input().split(' ')
    if d == '0' and n == '0':
        break
    n = n.replace(d,'')
    if n == '':
        n = '0'
    n = int(n)
    print(n)

    