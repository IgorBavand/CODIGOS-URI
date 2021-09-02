n = int(input())

for i in range(n):
    j1,e1,j2,e2 = input().split()
    n1,n2 = input().split()
    n1 = int(n1)
    n2 = int(n2)
    res = n1+n2
    if res%2==0 and e1 == 'PAR':
        print(j1)
    else:
        print(j2)
