n, d = input().split(' ')
n = int(n)
d = int(d)

while d != 0 and n != 0:
    for i in range(d):
        verificacao = 0
        jantares = input()
        if not '0' in jantares:
            verificacao = 1
    if(verificacao == 1):
        print('yes')
    else:
        print('no')
    n, d = input().split(' ')
    n = int(n)
    d = int(d)