a=int(input())
b=int(input())
list=[]
# list=[[100]*a]*b
# print(list)
for i in range(b):
    for j in range(a):
        list.append(100)
    print(list)
    for k in range(a):
       list.remove(100)