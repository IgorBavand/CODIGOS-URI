n = int(input())

for i in range(n):
    t1j1, x, t2j1 = input().split(' ')
    t2j2, x, t1j2 = input().split(' ')

    t1j1 = int(t1j1)
    t2j1 = int(t2j1)
    t2j2 = int(t2j2)
    t1j2 = int(t1j2)

    if t1j1+t1j2 > t2j1+t2j2:
        print('Time 1')
    elif t1j1+t1j2 < t2j1+t2j2:
        print('Time 2')
    else:
        if t1j2 > t2j1:
            print('Time 1') 
        elif t1j2 < t2j1:
            print('Time 2')
        else:
            print('Penaltis')
