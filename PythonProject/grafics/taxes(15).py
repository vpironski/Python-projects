import PySimpleGUI as ps 

city = ('Sofia','Varna', 'Plovdiv', )

layout = [
   [ps.Text('Quantity of sales:'), 
    ps.InputText('0',key='sale'),
    ps.Combo(city,readonly = True, default_value='Sofia',key='city')
   ],
   [ps.Text('Tax:',size=(9,1)),
    ps.Text('0',key = 'output',size=(25,1)),
    ps.Button('Calculate')
   ]
]

window = ps.Window('Tax calculater',layout)


while True:
    event, values = window.read()
    if event == ps.WIN_CLOSED:
        break
    elif event == 'Calculate':
        taxp = 0

        if values ['city'] == 'Sofia':
            if values ['sale'] <= 500:
                taxp = 5/100 * values ['sale']
            elif values ['sale'] > 500 and values ['sale'] <= 1000:
                taxp = 7/100 * values ['sale']
            elif values ['sale'] > 1000 and values ['sale'] <= 10000:
                taxp = 8/100 * values ['sale']
            elif values ['sale'] >10000:
                taxp = 12/100 * values ['sale']
       
       
        if values ['city'] == 'Plovdiv':
            if values ['sale'] <= 500:
                taxp = 5.5/100 * values ['sale']
            elif values ['sale'] > 500 and values ['sale'] <= 1000:
                taxp = 8/100 * values ['sale']
            elif values ['sale'] > 1000 and values ['sale'] <= 10000:
                taxp = 12/100 * values ['sale']
            elif values ['sale'] >10000:
                taxp = 14.5/100 * values ['sale']
        
        
        if values ['city'] == 'Varna':
            if values ['sale'] <= 500:
                taxp = 4.5/100 * values ['sale']
            elif values ['sale'] > 500 and values ['sale'] <= 1000:
                taxp = 7/100 * values ['sale']
            elif values ['sale'] > 1000 and values ['sale'] <= 10000:
                taxp = 10/100 * values ['sale']
            elif values ['sale'] >10000:
                taxp = 13/100 * values ['sale']


    tax = round(taxp,2)
    window['output'].update(str(tax) + 'BGN')
     

window.close()


