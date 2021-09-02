import math
while True:

    l,c,r1,r2 = input().split()
    l = int(l)
    c = int(c)
    r1 = int(r1)
    r2 = int(r2)

    if l == 0 and c == 0 and r1 == 0 and r2 == 0: break

    soma = r1+r2
    x = l-soma
    y = c-soma

    distancia = math.sqrt((x*x)+(y*y))

  
    if soma <= int(distancia):
        print('S')
    else:
        print('N')
        