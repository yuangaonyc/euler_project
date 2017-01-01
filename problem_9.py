for a in range(1,999):
	for b in range(1, 999):
		c = 1000 - a - b
		if c > 0 and a * a + b * b == c * c:
			print(a*b*c)
			break
	else:
		continue
	break