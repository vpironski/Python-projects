mounth = str(input("The mount is "))
day = int(input("The day is "))

if mounth == "January":
    if day > 31:
        print('Too many days')
    else:
     print('The season is winter')

elif mounth == 'February':
    if day >= 28:
        print('Too many days')
    else:
           print('The season is winter')


elif mounth == 'March':
    if day < 21:
        print('The season is winter')
    elif day >= 21:
        print('The season is spring')
    elif day > 31:
        print('Too many days')

elif mounth == 'April':
    if day > 30:
       print('Too many days')
    else: 
            print('The season is spring')

elif mounth == "May":
    if day > 31:
       print('Too many days')
    else:    
        print('The season is spring')

elif mounth == "June":
    if day < 21:
        print('The season is spring')
    elif day >= 21:
        print('The season is summer')
    elif day > 30:
       print('Too many days')

elif mounth == "July":
    if day > 31:
       print('Too many days')
    else:
       print('The season is summer')


elif mounth == 'August':
    if day > 31:
       print('Too many days')
    else:
            print('The season is summer')

elif mounth == 'September':
    if day < 21:
        print('The season is summer')
    elif day >= 21:
        print('The season is autumn')
    elif day > 30:
       print('Too many days')

elif mounth == 'October':
    if day > 31:
       print('Too many days')
    else:
            print('The season is autumn')

elif mounth == 'November':
    if day > 30:
       print('Too many days')
    else:
            print('The season is autumn')

elif mounth == 'December':
    if day < 21:
        print('The season is winter')
    elif day >= 21:
        print('The season is spring')
    if day > 31:
       print('Too many days')



    
