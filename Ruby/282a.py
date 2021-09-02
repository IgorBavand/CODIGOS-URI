n = int(input())

x = 0
for i in range(n):
    entrada = input()
    if '--' in entrada:
        x -=1
    if '++' in entrada:
        x +=1

print(x)