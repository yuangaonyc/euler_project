year = 1900
month = 1
day = 1
weekday = 1
c = 0

def add_day():
	global year, month, day, weekday, c

	if weekday == 7:
		weekday = 1
	else:
		weekday += 1

	if month == 12 and day == 31:
		year += 1
		month = 1
		day = 1
	elif month in [9, 4, 6, 11] and day == 30:
		month += 1
		day = 1
	elif month in [1, 3, 5, 7, 8, 10] and day == 31:
		month += 1
		day = 1
	elif year % 4 == 0 and month == 2 and day == 29:
		month += 1
		day = 1
	elif year % 4 != 0 and month == 2 and day == 28:
		month += 1
		day = 1
	else:
		day += 1

	if year >= 1901: 
		if day == 1 and weekday == 7:
			c += 1
			print("{}/{}/{}, {} counts:{}".format(month,day,year,weekday,c))

while not (year == 2000 and month == 12 and day == 31):
	add_day()

print('answer: {}'.format(c))