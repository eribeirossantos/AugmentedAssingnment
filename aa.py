number = "9, 223, 372, 036, 854, 775, 807"

cleanednumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        # cleanednumber = cleanednumber + number[i]
        cleanednumber += number[i]
        
nemNumber = int(cleanednumber)
print("The Number is {}".format(nemNumber))


x = 23
x += 1
print(x)

x -= 1
print(x)

x *= 2
print(x)