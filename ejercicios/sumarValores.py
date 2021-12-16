list = [] 
print('Enter a number and to exit write "enough" ')

while True:
    value = input('Enter a value ')
    if value == 'enough':
        break
    else:
        try:
            value = int(value)
            list.append(value)
        except: 
            print('Value invalid')
            exit()

result = 0
for x in list:
    result += x

print(result)