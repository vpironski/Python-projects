import PySimpleGUI as ps 


cities = ('Sofia', 'Plovdiv', 'Varna','Burgas','Pleven')
products = ('banana','water','juice','sweets','peanuts')
ps.theme('Reddit')

layout = [

    [ps.Text('Quantity:'), 
    ps.InputText('0',key = 'Quantity'), 
    ps.Combo(products,readonly = True, default_value='water',key='products'),
    ps.Combo(cities,readonly = True, default_value='Sofia',key='cities'),
    ],
    [ps.Text('Price:',size=(9,1)),
    ps.Text('0',key = 'output',size=(25,1)),
    ps.Submit('Calculate')]
]

window = ps.Window('Store',layout)

while True:
    event, values = window.read()
    if event == ps.WIN_CLOSED:
        break
    elif event == 'Calculate':
        price = 0


        if values['cities']=='Sofia':
            if values['products']=='banana':
                price = 1.5
            elif values['products']=='water':
                price = 0.8
            elif values['products']=='juice':
                price = 2.4
            elif values['products']=='sweets':
                price = 1.4
            elif values['products']=='peanuts':
                price = 2.3
        elif values['cities']=='Plovdiv':
            if values['products']=='banana':
                price = 1.6
            elif values['products']=='water':
                price = 0.6
            elif values['products']=='juice':
                price = 2.2
            elif values['products']=='sweets':
                price = 1.6
            elif values['products']=='peanuts':
                price = 2.5
        elif values['cities']=='Varna':
            if values['products']=='banana':
                price = 1.2
            elif values['products']=='water':
                price = 0.5
            elif values['products']=='juice':
                price = 2.5
            elif values['products']=='sweets':
                price = 1.1
            elif values['products']=='peanuts':
                price = 2.7
        elif values['cities'] == 'Burgas':
            if values['products']=='banana':
                price = 1.3
            elif values['products']=='water':
                price = 0.8
            elif values['products']=='juice':
                price = 2.8
            elif values['products']=='sweets':
                price = 1.0
            elif values['products']=='peanuts':
                price = 3.0
        elif values['cities'] == 'Pleven':
            if values['products']=='banana':
                price = 1.0
            elif values['products']=='water':
                price = 0.5
            elif values['products']=='juice':
                price = 2.9
            elif values['products']=='sweets':
                price = 1.3
            elif values['products']=='peanuts':
                price = 3.2

        all = round(price * float (values['Quantity']),2)
        window['output'].update(str(all) + 'BGN')


window.close()
            