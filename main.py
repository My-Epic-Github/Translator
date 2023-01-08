import PySimpleGUI as sg
import epictranslator as tr



def main():
    layout = [[sg.Button('Translator', key='butt')]]

    window = sg.Window('Tool Selector', layout)

    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED:
            break
        if event == 'butt':
            tr.translator()
            
            
            
            
            

        
        