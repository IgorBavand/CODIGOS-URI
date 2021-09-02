while True:
    try:

        n = int(input())
        pe_direito = []
        pe_esquerdo = []
        for i in range(n):
            num_pe = input()
            if num_pe[-1] == 'D':
                pe_direito.append(num_pe.split())
            else:
                pe_esquerdo.append(num_pe)
            
        #veri = 0
        while len(pe_direito) < 0:
            for k in range(len(pe_esquerdo)):
                print(pe_direito)
                print(pe_esquerdo)
                #if pe_direito[0][0] == pe_esquerdo[k][0]:
                #    print('tem um aqui o')
            print('ksnckdk')
            pe_direito.pop(0)
            
                


                
    
    except EOFError:
        break