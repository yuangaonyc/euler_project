def palindrome(st):
	if st[::-1] == st:
		return True
	else:
		return False

ans = 0
for i in range(100, 1000):
	for j in range(100, 1000):
		p = str(i * j)
		if palindrome(p) and int(p) > ans:
			ans = int(p)

print(ans)
