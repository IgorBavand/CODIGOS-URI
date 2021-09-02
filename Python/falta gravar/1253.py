qtd_testes = int(input())
alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in range(qtd_testes):
    palavra = input()
    tam_cifra = int(input())
    palavra = list(palavra)
    
    for tam_palavra in range(len(palavra)):
        calcular = alfabeto.index(palavra[tam_palavra])        
        letra_final = calcular - tam_cifra
        if letra_final < 0:
            letra_final +=26
            
        print(alfabeto[letra_final],end='')
    print()