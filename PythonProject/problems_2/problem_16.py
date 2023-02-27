type = str(input('Projection: '))
r = int(input('Number of rows: '))
c = int(input('Number of columbs: '))

if type == 'Premiere' or type == 'premiere':
    sum = (r*c) * 12
    print(round(sum,2),'lv')

elif type == 'Normal' or type == 'normal':
    sum = (r*c) * 7.5
    print(round(sum,2),'lv')

elif type == 'Dicount' or type == 'discount':
    sum = (r*c) * 5
    print(round(sum,2),'lv')

else:
    print('error')