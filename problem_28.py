d = 1001
num_of_layers = (d - 1) / 2

def layer_opener(layer_num):
	if layer_num == 0:
		return list(range(1,2))
	else:
		start_num = layer_opener(layer_num-1)[-1]+1
		layer_len = layer_num * 8
		end_num = start_num + layer_len
		return list(range(start_num,end_num))

def num_selector(layer_num):
	if layer_num == 0:
		return [0]
	else:
		return [-1, -1-(2*layer_num), -1-(2*layer_num)*2, -1-(2*layer_num)*3]

ans = 0
for layer_num in range(0,num_of_layers+1):
	print('procesing layer', layer_num)
	opened_layer = layer_opener(layer_num)
	num_idx = num_selector(layer_num)
	for i in num_idx:
		ans += opened_layer[i]
print(ans)