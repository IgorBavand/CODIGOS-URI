i = 1
l = 1
j = 7
aux = j
while i <= 9:
    for l in range(3):
        print('I={} J={}'.format(i,j))
        j-=1
    j = aux +2
    aux +=2

    i+=1