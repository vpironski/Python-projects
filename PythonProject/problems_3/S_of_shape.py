print("-----------------")
print("Square -> 1")
print("Triangle -> 2")
print("Rectangle -> 3")
print("-----------------")
name = int(input("Enter the name: "))

def square():
    a = int(input("a = "))
    S = a*a
    print(S)

def triangle():
    a = int(input("a = "))
    b = int(input("b = "))
    S = a*b/2
    print(S)

def rect():
    a = int(input("a = "))
    b = int(input("b = "))
    S = a*b
    print(S)


if (name == 1):
    square()

elif (name == 2):
    triangle()

elif (name == 3):
    rect()

