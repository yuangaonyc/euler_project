import math

ans = math.factorial(20 + 20)/ math.factorial(20)/ math.factorial(20)
print(ans)

# function to return all possibilities:
# 
# def all_perms(elements):
# 	if len(elements) <= 1:
# 		yield elements
# 	else:
# 		for perm in all_perms(elements[1:]):
# 			for i in range(len(elements)):
# 				yield perm[:i] + elements[0:1] + perm[i:]