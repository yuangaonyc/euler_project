def factor(num):
	factor_li = []
	i = 1
	while i <= num:
		if num % i == 0:
			factor_li.append(i)
		i += 1
	return factor_li

def is_prime(num):
	if len(factor(num)) > 2:
		return False
	else:
		return True 	

num = 600851475143
i = 1
while i < num:
	if num % i == 0 and is_prime(i):
		print i
	i += 1