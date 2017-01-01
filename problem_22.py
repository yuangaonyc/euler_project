input = open('p022_names.txt').read()
data = input.replace('"','').split(',')
data.sort()

letters = ['A','B','C','D','E','F','G','H','I','J',\
		   'K','L','M','N','O','P','Q','R','S','T',\
		   'U','V','W','X','Y','Z']

scores = list(range(1,27))

letter_score = zip(letters, scores)

letter_score = dict((letter,score) for letter,score in letter_score)

def name_score(name):
	res = 0
	for letter in name:
		res += letter_score[letter]
	return res

ans = 0

i = 0
while i < len(data):
	name = data[i]
	ans += (i+1) * name_score(name)
	print('processing', name, (i+1), name_score(name) )
	i += 1

print('answer', ans)
