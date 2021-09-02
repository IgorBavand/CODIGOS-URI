notas = []
n = 0.0
while(len(notas) != 2):
    n = float(input())
    if n < 0 or n > 10:
        print('nota invalida')
    else:
        notas.append(n)
print('media = {:.2f}'.format(sum(notas)/2))