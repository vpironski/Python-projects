first_name = input('first name: ')
last_name = input('last name: ')
age = int(input('age: '))
town = input('town: ')

print('Hi, my name is {0} {1}, I am a {2} year old person from {3}.'
.format(first_name,last_name,age,town))

print(str(first_name) + ' ' + str(last_name) + ' '+ str(age) + ' ' + str(town))