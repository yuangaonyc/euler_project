def fibonacci(a,b):
	return (a+b)

li = [1,2]
i = 0
while True:
	new_fib = fibonacci(li[i], li[i+1])
	if new_fib <= 4000000:
		li.append(new_fib)
	else:
		break
	i += 1

sum = 0
for num in li:
	if num % 2 == 0:
		sum += num

print(sum)
