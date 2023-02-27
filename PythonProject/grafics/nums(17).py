import PySimpleGUI as ps 

numbers = [1,2,3,4,5,6,7,8,9]
ps.theme('Reddit')

layout = [ 
    [ ps.Text('Number'), 
    ps.Combo(numbers,readonly = True, default_value='1',key='numbers'),
    ],
    [ps.Text('The number is pronounsed: '), 
    ps.Text(key = 'output',size = (10,1)),
    ps.Submit('Write')
    ],
    [ ps.Submit('done'),
    ]
]


window = ps.Window('English numbers',layout)


while True:
    event, values = window.read()
    if event == ps.WIN_CLOSED and event == 'done':
        break
    elif event == 'Write':
        word = str('none')
      
        if values['numbers'] == 1:
            word = str('One')

        elif values['numbers'] == 2:
            word = str('Two')

        elif values['numbers'] == 3:
            word = str('Three')

        elif values['numbers'] == 4:
            word = str('Four')

        elif values['numbers'] == 5:
            word = str('Five')

        elif values['numbers'] == 6:
            word = str('Six')

        elif values['numbers'] == 7:
            word = str('Seven')

        elif values['numbers'] == 8:
            word = str('Eight')

        elif values['numbers'] == 9:
            word = str('Nine')

    window['output'].update(str(word))

window.close()
