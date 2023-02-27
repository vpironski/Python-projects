
a = [2,4,8,10]
a.append(12)
a.append(15)
a.append(16)

print(a.count(2))
print(a.index(8))
print(min(a))
print(max(a))
a.pop(0)


print (a[1])

a[1] = 11
print(a)

s = list()
# s = []

s= [2, 4, 6, 8, 2]
s.append(22)      # добавя в края на
print(s)
s += [44, 88]     # добавя в края 44,88
print(s)
s.insert(0, 90)  # вмъква 90 на мястото на дадения индекс
print(s)
s.pop(0)         # изтрива първия елемент на списъка
print(s)
s.remove(2)      # изтрива елемента със стойност 2
print(s)
del s[4]         # премахва елемента с индекс 4
print(s)


# random list 
import random
list = []
  
for i in range(0,5):
   n = random.randint(1,10)
   list.append(n)
print(list)