numeros = []

for l in range(2):
    entrada = int(input())
    numeros.append(entrada)
    
numeros = sorted(numeros)

a = numeros[0]
b = numeros[1]
c=0
aux = 0


for i in range(a,b+1):
    if i%13!=0:
        c=c+i

print(c)