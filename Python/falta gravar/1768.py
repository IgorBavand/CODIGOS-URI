while True:
    try:

        n = int(input())

        calculo = n-1
        calculo = calculo/2
        calculo = int(calculo)
        aux = calculo

        i = 1

        while i <= n:
            print(' '*calculo, end='');
            print('*'*i)

            i = i + 2   
            calculo = calculo - 1 

        print(' '*aux,end='')
        aux = aux - 1
        print('*')
        
        print(' '*aux,end='')
        
        print('***')


        print('')




    except EOFError:
        break