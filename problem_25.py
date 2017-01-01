# run with python3
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
	if n == 0: return 0
	elif n == 1: return 1
	else: return fib(n-1) + fib(n-2)

i = 1
while len(str(fib(i))) < 1000:
	print('checking: {}th fib has length of {}'.format(i, len(str(fib(i)))))
	i += 1
print(i)