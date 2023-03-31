import copy
def fact(n):
    n=int(n)
    m= int(copy.copy(n))
    wynik = 0
    while m!=0:
        if wynik == 0:
            wynik = n
            m=m-1
        else:
            wynik=wynik*m
            m=m-1
    return wynik

import PySimpleGUI as sg
sg.theme("DarkAmber")
layout = [  [sg.Text('Factorial of which number? '), sg.InputText()],
            [sg.Button('Calculate'),],
            [sg.Text("Answer will appear here.", key="silnia")]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
    window["silnia"].update( fact(values[0]))
    print('Input:', values[0], "  Output:", fact(values[0]))

window.close()