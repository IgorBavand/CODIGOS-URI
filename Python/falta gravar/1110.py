numero = input()
while numero != '0':
    
    cartas = []
    descartes = []
    i = int(numero)
    
    while i >= 1:
        cartas.append(str(i))
        i-=1
    
    while len(cartas) > 1:
        descartes.append(cartas[len(cartas)-1])
        cartas.pop()       
        cartas.insert(0, cartas[len(cartas)-1])
        cartas.pop()

    print('Discarded cards: ', end='')
    for d in range(len(descartes)):
        if d == len(descartes)-1:
            print('{}'.format(descartes[d]), end='')
        else:
            print('{}, '.format(descartes[d]), end='')
        
    print('')
    print('Remaining card: {}'.format(cartas[0]))
    numero = input()

    
    
