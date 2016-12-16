def prime_factorization(num):
	factor_list = []
	if num == 1:
		return []
	for i in range(2, num+1):
		if num % i == 0:
			factor_list.append(i)
			factor_list = factor_list + prime_factorization(num/i)
			return factor_list

result_list = []

for num in range(1, 21):
	factor_list = prime_factorization(num)
	for i in factor_list:
		while factor_list.count(i) > result_list.count(i):
			result_list.append(i)

print(reduce(lambda x,y: x*y, result_list, 1))