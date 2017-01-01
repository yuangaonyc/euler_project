# Q1
def puppy_golden_age(input_arr):
	result = {}
	i = 0
	while i < len(input_arr):
		j = i + 1
		while j < len(input_arr):
			score = sum(input_arr[i:j+1])
			result[(i,j)] = score
			j += 1
		i += 1

	return list(max(result, key=result.get))

# print puppy_golden_age([100, -101, 200, -3, 1000])
# print puppy_golden_age([5, 3, -5, 1, 19, 2, -4])


# Q2
def combine_arrays(a, b):
	result = [a[0]]

	for item in a[1:]:
		i = 0
		while i < len(result) and item > result[i]:
				i += 1
		result.insert(i, item)

	for item in b:
		i = 0
		while i < len(result) and item > result[i]:
				i += 1
		result.insert(i, item)

	return result

# print combine_arrays([1,3,5], [2,4,6])
# print combine_arrays([3,5,1], [4,6,2])




# Q3
def subsets(input_arr):
    if input_arr == []:
        return [[]]

    x = subsets(input_arr[1:])

    return x + [[input_arr[0]] + y for y in x]

# print subsets(["a", "b", "c"])