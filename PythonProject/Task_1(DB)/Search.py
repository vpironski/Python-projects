import io

f = io.open("The_Machine_That_Won_the_War_AA.txt", "r", encoding="utf-8")

file = f.read()
print(file)
f.close()

countForwards = 0
countBackwards = 0

for i,j in enumerate(file):

    if file[i] == 'в' and file[i+1] == 'а' and file[i+2] == 'к':
        countForwards += 1

reverse = []

for l in reversed(list(file)):
    reverse.append(l)




for i,j in enumerate(reverse):
        if reverse[i] == 'в' and reverse[i+1] == 'а' and reverse[i+2] == 'к':
            countBackwards += 1
    
fullCount = countForwards + countBackwards


print("The count of the word going forward is: ", countForwards)
print("The count of the word going backward is: ", countBackwards)
print("The sum of the counts is: ", fullCount)





