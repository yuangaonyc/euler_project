num = 2
sm =0

def is_prime(num):
	for i in range(2, int(num ** 0.5)+1):
		if num % i == 0:
			return False
	return True

while num < 2000000:
	if is_prime(num):
		sm += num
		print(num, sm)
	num += 1