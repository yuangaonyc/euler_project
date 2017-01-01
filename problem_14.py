def op(num):
	global cnt
	if num % 2 == 0:
		cnt += 1
		return num / 2
	else:
		cnt += 1
		return num * 3 + 1
	
max_cnt = 0
ans = 0

for num in range(1, 1000000):
	print("processing", num)
	cnt = 1
	num_copy = num
	while num != 1:
		num = op(num)
		if cnt > max_cnt:
			max_cnt = cnt
			ans = num_copy

print("answer", ans, "with max_cnt", max_cnt)