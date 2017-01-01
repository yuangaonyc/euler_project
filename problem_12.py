import math

def triangle(num):
	return num*(num+1)/2

def divisor_num(num):
	cnt = 0
	for i in range(1, int(math.sqrt(num)+1)):
		if num % i == 0:
			cnt += 2
	return cnt

i = 2
while divisor_num(triangle(i)) <= 500:
	i += 1
	print(i)

print('answer', triangle(i))

