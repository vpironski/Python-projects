wine = 300
beer = 200
number = 0
wineDeliv = 0
wineOrder = 0
beerDeliv = 0
beerOrder = 0

while(True):
    line = input()
    if(line == "END"):
        break

    line = line.split(": ")
    number = int(line[1])

    if(line[0] == "Wines"):
        if(number > 0):
            wine += number
            wineDeliv += 1
        elif(number<0):
            wine += number
            wineOrder +=1
    elif(line[0] == "Beers"):
        if(number > 0):
            beer += number
            beerDeliv += 1
        elif(number<0):
            beer += number
            beerOrder +=1

print("Wines: " , wine)
print("Deliveries: " , wineDeliv)
print("Orders: " , wineOrder )
print("Beers: " , beer)
print("Deliveries: " , beerDeliv)
print("Orders: " , beerOrder )


    