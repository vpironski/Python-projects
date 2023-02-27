# Тяло на функцията;
def disco ():
    string = '-- inside f():'
    print(string)


print('Before calling f()')
# Извикване на функцията;
disco()
print('After calling f()')



def f (quantity, item, price):
    print(f'{quantity} {item} cost ${price:.2f}')

f(6,'bananas',1.65)
f(item = 'bananas', price = 1.65, quantity = 6, )


#----------------------------------------------------------------
def say_hi(user,age):
  print(f'Hello, Im {user}')
  print(f'Im {age}')


user = str(input('Please enter name: '))
age = int(input('Please enter age: '))
say_hi()


# задачи с функции "function()"

############################################################################################################
#функция, която намира средно аритметичното на 3 числа

def avarage(x,y,z):
    return (x+y+z)/3

x = int(input("Number one is: ")) 
y = int(input("Number two is: "))
z = int(input("Number three is: "))

print("The avarage value of the three numbers is: ", avarage(x,y,z))


############################################################################################################
# функция, която казва здравей, спрямо въведеното име

def hi(first_name,last_name):
    print("----------------------------------------------")
    print(f"Hello {first_name} {last_name}!")
    print("Welcome to the Matrix")
    print("----------------------------------------------")

first_name = input("First Name: ")
last_name = input("Last Name: ")

hi(first_name,last_name)


############################################################################################################
# функия, която връща квадрата на всяка стойност

def square(num):
    return num**2

num = int(input("Number: "))
print("----------------------------------------------")
print(f"The square of {num} is: ", square(num))



