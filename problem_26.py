from decimal import *
getcontext().prec = 2000

def super_check(pattern, string):
	i = 0
	check = True
	while check and i <= len(string)-len(pattern):
		if string[i:i+len(pattern)] != pattern:
			check = False
		i += len(pattern)
	return check

def recurring(digits):
	k = int(len(digits))
	if k < 2000:
		return ''
	for l in range(1, k):
		for i in range(0, k):
			if digits[i:i+l] == digits[i+l:i+l+l]:
				if super_check(digits[i:i+l], digits[i+l:]):
					return digits[i:i+l]

max_l = 0
ans_num = 0
for num in range(2,1000):
	print('processing: {}'.format(num))
	digits = str(Decimal(1)/Decimal(num))[2:]
	res = len(recurring(digits))
	if res > max_l:
		max_l = res
		ans_num = num

print('1/{} has {} recurring digits'.format(ans_num, max_l))
