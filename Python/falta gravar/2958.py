l,c = input().split(' ')
l = int(l)
c = int(c)
valores = []
pvida = []
pdis = []
for i in range(l):
	aux = list(map(str, input().split(' ')))
	for k in aux:
		if k[1] == 'V':
			pvida.append(k[0])
		else:
			pdis.append(k[0])

pvida = sorted(pvida, reverse=True)
pdis = sorted(pdis, reverse=True)
for vida in pvida:
	print('{}V'.format(vida))
for dis in pdis:
	print('{}D'.format(dis))
