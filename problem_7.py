num = 2
cnt = 0

def is_prime(num):
	for i in range(2, num):
		if num % i == 0:
			return False
	return True

while cnt < 10001:
	if is_prime(num):
		cnt += 1
		print(cnt, num)
	num += 1