import itertools

a = list(range(2,101))
b = list(range(2,101))

ab = list(itertools.product(a, b))

res = set()
for a,b in ab:
	print('processing', a, b)
	res.add(a ** b)

print('counting items...')
print(len(res))
