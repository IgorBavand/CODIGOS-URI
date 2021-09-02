n = int(input())

for i in range(n):
    a,b = input().split(' ')

    a = list(a)
    b = list(b)
    excluir = len(a) - len(b)
    for l in range(excluir):
        a.pop(0)
    
    if a==b:
       print('encaixa')
    else:
       print('nao encaixa')
