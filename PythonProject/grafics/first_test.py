import PySimpleGUI as ps 

ps.theme('Reddit')

layout = [
    [ps.Text(' ',size = (4,1)),
    ps.Text('My first try at making windows')] , 
    [ps.Text(' ',size = (12,1)),
    ps.Button('done')]
]

window = ps.Window('Hello from Vihren',layout,size = (250,100))

while True:
    event, values = window.read()

    if event == 'done' or event == ps.WIN_CLOSED:
        break

window.close() 