city = str(input('City: '))
s = float(input('Sales: '))


if city == 'Sofia':
    if s <= 500:
        commission = 5/100 * s
        print(round(commission,2),'lv')
    elif s > 500 and s <= 1000:
        commission = 7/100 * s
        print(round(commission,2),'lv')
    elif s > 1000 and s <= 10000:
        commission = 8/100 * s
        print(round(commission,2),'lv')
    elif s > 10000:
        commission = 12/100 * s
        print(round(commission,2),'lv')
    else:
        print('Error')

elif city == 'Plovdiv':
    if s <= 500:
        commission = 5.5/100 * s
        print(round(commission,2),'lv')
    elif s > 500 and s <= 1000:
        commission = 8/100 * s
        print(round(commission,2),'lv')
    elif s > 1000 and s <= 10000:
        commission = 12/100 * s
        print(round(commission,2),'lv')
    elif s > 10000:
        commission = 14.5/100 * s
        print(round(commission,2),'lv')
    else:
        print('Error')

elif city == 'Varna':
     if s <= 500:
        commission = 4.5/100 * s
        print(round(commission,2),'lv')
     elif s > 500 and s <= 1000:
        commission = 7.5/100 * s
        print(round(commission,2),'lv')
     elif s > 1000 and s <= 10000:
        commission = 10/100 * s
        print(round(commission,2),'lv')
     elif s > 10000:
        commission = 13/100 * s
        print(round(commission,2),'lv')
     else:
        print('Error')

else:
    print('error')
    
