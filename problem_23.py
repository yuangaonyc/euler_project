import math

def is_abundant(num):
	divi_sum = 0
	for i in range(1, int(math.sqrt(num)+1)):
		if num % i == 0:
			divi_sum += i
			j = num / i
			if j != i:
				divi_sum += num / i
	divi_sum -= num
	return divi_sum > num

non_abundant_sum = 0
for num in range(1, 28123):
	print("checking", num)
	for i in range(1, int(num/2)+1):
		if is_abundant(i) and is_abundant(num-i):
			break
	else:
		non_abundant_sum += num
print("answer", non_abundant_sum)