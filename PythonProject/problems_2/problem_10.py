

name = str(input('Your name is: '))
age = int(input('Your age is: '))
sex = str(input('Your sex is: '))

if sex == 'male' and age >= 16:
    print('Hello Mr.',name)

elif sex == 'male' and age < 16:
     print('Hello Master',name)

elif sex == 'female' and age >= 16:
    print('Hello Ms.',name)
    
elif sex == 'female' and age < 16:
        print('Hellow Miss',name)