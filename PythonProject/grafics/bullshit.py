import PySimpleGUI as bullshit 

bullshit.theme ("Reddit")

layout = [
    [bullshit.Text(' ',size = (5,1)),
    bullshit.Text('This is my bullshit program')],
    [bullshit.Text(' ',size = (5,1)),
    bullshit.Button('Im ready for the bullshit')]
]

window = bullshit.Window('Random bullshit go',layout,size=(250,100))

while True:
    event, values = window.read()
    if event == bullshit.WIN_CLOSED or event == 'Im ready for the bullshit':
        break


window.close() 