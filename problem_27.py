import math

def is_prime(num):
	if num <2:
		return False
	if num == 2:
		print('ay')
		return True
	else:
		for i in range(2, int(math.sqrt(num)+1)):
			if num % i == 0:
				return False
		return True

max_n = 0
ans_a = 0
ans_b = 0

for a in range(-999,1000):
	for b in range(-1000,1001):

		n = 0
		while is_prime(n**2+a*n+b):
			n += 1
			print('checking: a = {}, b = {}, n = {}'.format(a,b,n))

		if n > max_n:
			max_n = n
			ans_a = a
			ans_b = b
print('answer: a = {}, b = {}, max_n = {}, a*b = {}'.format(ans_a,ans_b,max_n,ans_a*ans_b))
