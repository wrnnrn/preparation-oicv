n = int(input("Number: "))
x = 0
t1 = 0
t2 = 1

while True:
	x = x +1
	if x == n:
		break

	tf = t1+t2
	t1 = t2
	t2 = tf
	tf = t1+t2
	print(tf)