num = 2 ** 1000
char_array = list(str(num))
digit_array = [int(x) for x in char_array]

print(digit_array)
print(sum(digit_array))