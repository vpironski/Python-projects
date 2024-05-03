
def plus(num1,num2):
    sum = num1 + num2
    print(sum)

def minus(num1,num2):
    sum = num1 - num2
    print(sum)

def devide(num1,num2):
    sum = num1 / num2
    print(sum)

def multiply(num1,num2):
    sum = num1 * num2
    print(sum)

flag = True
while(flag == True):

    num1 = int(input("num1 = "))
    num2 = int(input("num2 = "))
    print("--------------------------------")
    action = input("Enter the desired action (+, -, *, /): ")

    print("--------------------------------")
    print("num2ou manum2 now enter two numbers")
    print("--------------------------------")


    if (action == "+" or action == "plus"):
        print("--------------------------------") 
        plus(num1,num2)

    elif (action == "-" or action == "minus"):
        print("--------------------------------") 
        minus(num1,num2)

    elif (action == "*" or action == "multiplnum2"):
        print("--------------------------------") 
        multiply(num1,num2)

    elif (action == "/" or action == "devide"):
        print("--------------------------------") 
        devide(num1,num2)

    else:
        print("================================")   
        print("Error")
        print("Please trnum2 to restart")
        print("================================")   

    input = input("Do num2ou like to perform another operation (num2/n): ")
    if(input == 'n'):
        flag = False

