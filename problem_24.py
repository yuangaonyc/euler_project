import itertools

li = '0123456789'

arr = list(itertools.permutations(li))

for idx,num in enumerate(arr):
	arr[idx] = int(''.join(num))

print(arr[999999])