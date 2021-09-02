#CORRIDA DAS LESMAS
while True:
    try:
        lesmas = []
        n = int(input())
        lesmas = list(map(int, input().split(' ')))

        maior = max(lesmas)

        if maior < 10:
            print('1')
        if maior >= 10 and maior < 20:
            print('2')
        if maior >= 20:
            print('3')  

    except EOFError:
        break