import math


print("--------------------------------")
action = input("Enter the desired action: ")

print("--------------------------------")
print("You may now enter two numbers")
print("--------------------------------")

def plus(x,y):
    sum = x + y
    print(sum)

def minus(x,y):
    sum = x - y
    print(sum)

def devide(x,y):
    sum = x / y
    print(sum)

def multiply(x,y):
    sum = x * y
    print(sum)

def procent(x,y):
    sum = (x*100)/y 
    print(sum,"%")  

def reverse_procent(x,y):
    sum = (x/100)*y
    print(sum)     

def power(x):
    sum = x**2
    print(sum)  

def root(x):
    sum =  math.sqrt(x)
    print(sum) 



if (action == "+" or action == "plus"):
    x = int(input("x = "))
    y = int(input("y = "))
    print("--------------------------------") 
    plus(x,y)

elif (action == "-" or action == "minus"):
    x = int(input("x = "))
    y = int(input("y = "))
    print("--------------------------------") 
    minus(x,y)

elif (action == "*" or action == "multiply"):
    x = int(input("x = "))
    y = int(input("y = "))
    print("--------------------------------") 
    multiply(x,y)

elif (action == "/" or action == "devide"):
    x = int(input("x = "))
    y = int(input("y = "))
    print("--------------------------------") 
    devide(x,y)

elif (action == "%" or action == "procent"):
    x = int(input("x = "))
    y = int(input("y = "))
    print("--------------------------------")     
    procent(x,y)

elif (action == "r%" or action == "reverse_procent"):
    x = int(input("x = %"))
    y = int(input("y = "))
    print("--------------------------------")     
    reverse_procent(x,y)    

elif (action == "^2" or action == "**2" or action == "power of two"):
    x = int(input("x = "))
    print("--------------------------------")
    power(x)

elif (action == "√" or action == "//2" or action == "squery root"):
    x = int(input("x = "))
    print("--------------------------------") 
    root(x)

else:
    print("================================")   
    print("Error")
    print("Please try to restart")
    print("================================")   


