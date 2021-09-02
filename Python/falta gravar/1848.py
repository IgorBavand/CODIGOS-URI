gritos = 0
soma = 0
acao = 'caw caw'
while gritos < 3:
    acao = input()
    if acao == 'caw caw':
	    print(soma)
	    gritos+=1
	    soma = 0
    else:
        if acao[2] == '*':
            soma+=1
        if acao[1] == '*':
            soma+=2
        if acao[0] == '*':
            soma+=4

    

         