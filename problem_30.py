# There is a magical point where f(x) = x and 
# f(x) = sum(digit_in_x ** 5) intercept for the last 
# time and 
res = []

def func(i):
	arr = list(str(i))
	opt = 0
	for num in arr:
		opt += int(num) ** 5
	return opt

i = 2
while i<1000000:
	print('processing', i, 'current_res_list', res)
	if func(i) == i:
		res.append(i)
	i += 1

print('answer', sum(res))