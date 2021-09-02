n = int(input())
dias = []
precos = []
for i in range(n):
    frutas = []
    preco = float(input())
    precos.append(preco)
    frutas = list(map(str, input().split(' ')))
    qtd = len(frutas)
    dias.append(qtd)

media_f = sum(dias)/n
media_p = sum(precos)/n
for l in range(len(dias)):
    print('day {}: {} kg'.format(l+1,dias[l]))


print('{:.2f} kg by day'.format(media_f))
print('R$ {:.2f} by day'.format(media_p))
