read_first_d = {'0': '',
				'1': 'one',
				'2': 'two',
				'3': 'three',
				'4': 'four',
				'5': 'five',
				'6': 'six',
				'7': 'seven',
				'8': 'eight',
				'9': 'nine'}

read_teens = {'0': 'ten',
			  '1': 'eleven',
			  '2': 'twelve',
			  '3': 'thirteen',
			  '4': 'fourteen',
			  '5': 'fifteen',
			  '6': 'sixteen',
			  '7': 'seventeen',
			  '8': 'eighteen',
			  '9': 'nineteen',}

read_second_d = {'0': '',
				 '2': 'twenty',
				 '3': 'thirty',
				 '4': 'forty',
				 '5': 'fifty',
				 '6': 'sixty',
				 '7': 'seventy',
				 '8': 'eighty',
				 '9': 'ninety'}

read_third_d =  {'1': 'onehundred',
				 '2': 'twohundred',
				 '3': 'threehundred',
				 '4': 'fourhundred',
				 '5': 'fivehundred',
				 '6': 'sixhundred',
				 '7': 'sevenhundred',
				 '8': 'eighthundred',
				 '9': 'ninehundred'
}

def read(num):
	num = str(num)
	if len(num) == 1:
		return read_first_d[num]
	elif len(num) == 2 and num[0] == '1':
		return read_teens[num[1]]
	elif len(num) == 2 and num[0] != '1':
		return read_second_d[num[0]] + read_first_d[num[1]]
	elif len(num) == 3 and num[1] == '0' and num[2] == '0':
		return read_third_d[num[0]]
	elif len(num) == 3 and num[1] == '1':
		return read_third_d[num[0]] + 'and' + read_teens[num[2]]
	elif len(num) == 3 and (num[1] != '0' or num[2] != '0'):
		return read_third_d[num[0]] + 'and' + read_second_d[num[1]] + read_first_d[num[2]]
	elif num == '1000':
		return 'onethousand'
	else:
		return '***********************************'

res = ''
for i in range(1,1001):
	res += read(i)

print('answer', len(res))