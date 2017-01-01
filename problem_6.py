def sum_o_square(num_of_items):
	opt = 0
	for i in range(1,num_of_items+1):
		opt += i * i
	return opt

def square_o_sum(num_of_items):
	opt = 0
	for i in range(1, num_of_items+1):
		opt += i
	return opt * opt

print(square_o_sum(100) - sum_o_square(100))