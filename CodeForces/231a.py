n = int(input())

cont = 0
for i in range(n):
    n1,n2,n3 = input().split()
    problema = 0
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    problema = n1+n2+n3

    if problema >= 2:
        cont+=1

print(cont)

    