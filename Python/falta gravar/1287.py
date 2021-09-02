while True:
    try:
        def ehnumero(entrada):
            try:
                int(entrada)
            except ValueError:
                return False
            return True

        numero = input()

        numero = numero.replace('o','0')
        numero = numero.replace('O','0')
        numero = numero.replace('l','1')
        numero = numero.replace(' ','')
        numero = numero.replace(',','')

        if ehnumero(numero):
            if int(numero) > 2147483647:
                print('error')
            else:
                print(int(numero))
            
        else:
            print('error')
    except EOFError:
        break


