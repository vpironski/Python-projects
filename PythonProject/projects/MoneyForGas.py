import PySimpleGUI as psg
from matplotlib.pyplot import psd

layout = [
    [psg.Text(' ',size = (5,1)),
    psg.Combo(('Shell','Lukoil','OMV','Petrol'),'Shell'),]
    [psg.Text(' ',size = (5,1)),
]
]

window = psg.Window('MoneyForGas',layout,size=(250,100))

while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED or event == 'Im ready for the bullshit':
        break


window.close() 