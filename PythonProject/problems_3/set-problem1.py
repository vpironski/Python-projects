a = set(())

num1 = int(input("num1 = "))
num2 = int(input("num2 = "))
num3 = int(input("num3 = "))
print("-------------------")

for i in range(1,7):
    b = int(input())
    a.add(b)
print("-------------------")
print(a)
print("-------------------")

if num1 in a:
    print(num1, 'is in a')
elif num1 not in a:
    print(num1, 'is not in a')
print("-------------------")

if num2 in a :
    print(num2, 'is in a')
elif num2 not in a :
    print(num2,'is not in a')
print("-------------------")

if num3 in a:
    print(num3,'is in a')
elif num3 not in a :
    print(num3,'is not in a')
print("-------------------")


