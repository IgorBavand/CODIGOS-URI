while True:
    d,n = input().split(' ')
    if d == '0' and n == '0':
        break
    n = n.replace(d,'')
    if n == '':
        n = '1'
    print(int(n))
