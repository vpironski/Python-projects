fruit = str(input('Fruit: '))
week = str(input('Day of the week: '))
quantity = float(input('How much would you like: '))


if week == 'Monday' or week == 'Tuesday' or week == 'Wednesday' or week == 'Thursday'  or week == 'Friday':
    if fruit == 'banana':
        price = quantity * 2.5
        print(round(price,2),'lv')
    elif fruit == 'apple':
        price = quantity * 1.2
        print(round(price,2),'lv')
    elif fruit == 'orange':
        price = quantity * 0.85
        print(round(price,2),'lv')
    elif fruit == 'grapefruit':
        price = quantity * 1.45
        print(round(price,2),'lv')
    elif fruit == 'kiwi':
        price = quantity * 2.70
        print(round(price,2),'lv')
    elif fruit == 'pineapple':
        price = quantity * 5.5
        print(round(price,2),'lv')
    elif fruit == 'grapes':
        price = quantity * 3.85
        print(round(price,2),'lv')
    else:
        print('Error')

elif week == 'Saturday' or week == 'Sunday':
    if fruit == 'banana':
        price = quantity * 2.7
        print(round(price,2),'lv')
    elif fruit == 'apple':
        price = quantity * 1.25
        print(round(price,2),'lv')
    elif fruit == 'orange':
        price = quantity * 0.9
        print(round(price,2),'lv')
    elif fruit == 'grapefruit':
        price = quantity * 1.6
        print(round(price,2),'lv')
    elif fruit == 'kiwi':
        price = quantity * 3
        print(round(price,2),'lv')
    elif fruit == 'pineapple':
        price = quantity * 5.6
        print(round(price,2),'lv')
    elif fruit == 'grapes':
        price = quantity * 4.2
        print(round(price,2),'lv')
    else:
        print('Error')

else:
    print('error')


