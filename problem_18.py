input = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

test_input = '''3
7 4
2 4 6
8 5 9 3'''

data = input.split("\n")
data = [x.split(" ") for x in data]
for idr,row in enumerate(data):
	for idx,x in enumerate(row):
		data[idr][idx] = int(data[idr][idx])

row_id = 0
item_id = 0 
routes = {str(data[row_id][item_id]) : [row_id,item_id]}
while routes.values()[0][0] < len(data)-1:
	for path in routes.keys():
		row_id_new = routes[path][0]+1
		item_id_new = routes[path][1]
		routes[path+" "+str(data[row_id_new][item_id_new])] = [row_id_new,item_id_new]
		item_id_new = routes[path][1] + 1
		routes[path+" "+str(data[row_id_new][item_id_new])] = [row_id_new,item_id_new]
		routes.pop(path, None)
for key,value in routes.iteritems():
	print(key,value)
ans = 0
for path in routes:
	nums = [int(x) for x in path.split(' ')]
	total = sum(nums)
	if total > ans:
		ans = total
print(ans)