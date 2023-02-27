

city = str(input('Which city would you like: '))
product = str(input('The product is: '))
quantity = float(input('How much would you like: '))


if city == 'Sofia':
    if product == 'coffee':
        price = quantity * 0.50 
        print(price,"lv")
    elif product == 'water':
        price = quantity * 0.80
        print(price,"lv")
    elif product == 'beer':
        price = quantity * 1.20
        print(price,"lv")
    elif product == 'sweets':
        price = quantity * 1.45
        print(price,"lv")
    elif product == 'peanuts':
        price = quantity * 1.60
        print(price,"lv")
    else:
        print('Sorry you have entered the wrond product')


elif city == 'Plovdiv':
    if product == 'coffee':
        price = quantity * 0.40
        print(price,"lv")
    elif product == 'water':
        price = quantity * 0.70
        print(price,"lv")
    elif product == 'beer':
        price = quantity * 1.15
        print(price,"lv")
    elif product == 'sweets':
        price = quantity * 1.30
        print(price,"lv")
    elif product == 'peanuts':
        price = quantity * 1.50
        print(price,"lv")
    else:
        print('Sorry you have entered the wrond product')


elif city == 'Varna':
    if product == 'coffee':
      price = quantity * 0.45
      print(price,"lv")
    elif product == 'water':
        price = quantity * 0.70
        print(price,"lv")
    elif product == 'beer':
        price = quantity * 1.10
        print(price,"lv")
    elif product == 'sweets':
        price = quantity * 1.35
        print(price,"lv")
    elif product == 'peanuts':
        price = quantity * 1.55
        print(price,"lv")
    else:
        print('Sorry you have entered the wrond product')


else:
    print('Sorry you have entered the wrong city, or have commited an error while typing')


    
