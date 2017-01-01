def factorial(num):
	if num == 1:
		return 1
	else:
		return num * factorial(num-1)

res = factorial(100)
arr = list(str(res))
ans = sum([int(x) for x in arr])

print(ans)