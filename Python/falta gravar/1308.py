def somatorio(numero):
    sum = 0
    for l in range(1,numero+1):
        sum = sum + l
    return sum


def qtd_filas(qtd_guerreiros):
    cont = 1
    while somatorio(cont) < qtd_guerreiros:
        cont+=1
    if somatorio(cont) != qtd_guerreiros:
        return cont - 1
    else:
        return cont



n = int(input())

for i in range(n):
    qtd_guerreiros = int(input())
    print(qtd_filas(qtd_guerreiros))
