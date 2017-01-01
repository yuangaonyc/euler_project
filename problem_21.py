def d(num):
	rtn = 0
	for i in range(1, num):
		if num % i == 0:
			rtn += i
	return rtn

d_dict = {}
for i in range(1, 10000):
	d_dict[i] = d(i)

ans = 0

for num1,d1 in d_dict.iteritems():
	for num2,d2 in d_dict.iteritems():
		if num1 != d1 and num2 != d2 and num1 == d2 and num2 == d1:
			ans += num1
			print(num1)

print("answer", ans)