x = int(input())
total = 0
for i in range(x):
	t,d = input().split(' ')
	t = int(t)
	d = int(d)
	total += (d*t)
print(total)	
