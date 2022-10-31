n, m = map(int, input().split())
list = []
list_n = []

for i in range(m):
	a, b = input().split()
	b_n = int(b)
	list.append(a)
	
	if(a == 'pay' or a == 'reservation'):
		b_n = -b_n
	list_n.append(b_n)
	print(i)
	
print(list)
while 'deposit' in list or n + list_n[0] >= 0:
	if n + list_n[0] < 0:
		if list[0] == 'reservation':
			temp1 = list[0]
			list[0] = list[1]
			list[1] = temp1
			
			temp2 = list_n[0]
			list_n[0] = list_n[1]
			list_n[1] = temp2
			
		if list[0] == 'pay':
			list.pop(0)
			list_n.pop(0)
			
		
	if n + list_n[0] >= 0:
		n += list_n.pop(0)
		list.pop(0)
		
print(n)
		
			
			
