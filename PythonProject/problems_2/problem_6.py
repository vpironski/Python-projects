
m = float(input('meters = '))
unit = str(input('unit -> '))



if unit == 'mm' :
    print('mm =', (m*1000))
elif unit == 'cm':
    print('cm =', (m*100))
elif unit == 'mi':
    print('mi =',round(m*0.000621371192,2))
elif unit == 'in':
    print('in =',round(m*39.3700787,2))
elif unit == 'km':
    print('km =',(m*0.001))
elif unit == 'yd':
    print('yd = ',round(m*1.0936133))
elif unit == 'ft':
    print(round(m*3.2808399))