n = float(input())


vetor = []
for i in range(100):
    vetor.append(n)
    n = n/2
   

for l in range(100):
    print('N[{}] = {:.4f}'.format(l,vetor[l]))
