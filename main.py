from googletrans import Translator
import PySimpleGUI as sg
import images
import pyperclip
import winshell, os, win32com.client
import time
import pyttsx3





iconlol = images.icon
desk = winshell.desktop()
engine = pyttsx3.init()
def talk(text):
    engine.say(text)
    engine.runAndWait()


path = os.path.join(desk, 'Translator.lnk')
target = f'{desk}\Python-Translator\dist\Translator.exe'
icon = f'{desk}\Python-Translator\shortcut-icon.ico'

shell = win32com.client.Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.IconLocation = icon
shortcut.save()


try:
    f = 'Arial', 10, 'bold'
    tf = 'Impact ', 12, 'bold', 'underline'
    theme = sg.theme('DarkGrey9')
    pf = 'Arial', 10, 'bold'


    layout = [
            [sg.Combo(['Auto','English', 'French','Spanish','Arabic', 'Dutch', 'Japanese', 'Russian', 'Serbian', 'Romanian', 'Bosnian', 'Finnish', 'Italian', 'German', ], font=f, key='langin', auto_size_text=True), sg.Combo(['English', 'French','Spanish','Arabic', 'Dutch', 'Japanese', 'Russian', 'Serbian', 'Romanian', 'Bosnian', 'Finnish', 'Italian', 'German', ], font=f, key='langout', pad=(283, 0))],
            [sg.Multiline('Translation Input',key='in', size=(40, 15), enable_events=True, font=f, no_scrollbar=True, right_click_menu=['&Right', ['&Copy All', '---', '&Paste', '---', '&Swap::1', '---', '&Clear::1', '---', '&Clear All', '---','&TTS', '---', '&Help']]), sg.Button('Translate', key='butt'), sg.Multiline('Translation Output', key='out', size=(40, 15 ), enable_events=True, font=f, no_scrollbar=True,right_click_menu=['&Right',['&Copy All::copy2','---', 'Paste::2', '&Swap::1', '---', '&Clear::2', '---', '&Clear All', '---', '&TTS::2', '---', '&Help']])],
            [sg.Button('<-->', key='invert', pad=(309,10), size=(5,1), font=f)],
            # [sg.Image(images.cheese), sg.Image(images.cheese)]
            ]
            

    window = sg.Window('Translator', layout, use_custom_titlebar=True, titlebar_font=tf, resizable=False, titlebar_background_color='Gray', titlebar_icon=iconlol, titlebar_text_color='white')

    while True:
        event, values = window.read()
        
        
        if event == sg.WIN_CLOSED:
            break
        
        if event == 'butt':
            try:
                tra = Translator()
                tr = tra.translate(values['in'], dest=values['langout'], src=values['langin'])
                window['out'].update(f'{tr.text}')
                
                
                
                    
            except Exception as e:
                print(e)
                
        
        if event == 'invert':
            window['langin'].update(values['langout'])
            window['langout'].update(values['langin'])
            
        
        
        elif event == 'Copy All':
            pyperclip.copy(values['in'])
            
        elif event == 'Copy All::copy2':
            pyperclip.copy(values['out'])
            
        elif event == 'Paste':
            window['in'].update(pyperclip.paste())
        
        elif event == 'Paste::2':
            window['out'].update(pyperclip.paste())
        
        elif event == 'Swap::1':
            window['in'].update(values['out'])
            window['out'].update(values['in'])
        
        elif event == 'Clear::1':
            window['in']('')
        
        elif event == 'Clear::2':
            window['out']('')
            
        elif event == 'Clear All':
            window['in']('')
            window['out']('')
        
        elif event == 'Help':
            sg.popup_ok("This is a crappy translator I made. If the language you want to translate isn't listed just type it in yourself and it will probably work. Note: TTS won't work on most non-latin alphabets, so don't expect it to read out something in russian. Also probably won't be the most accurate with pronounciations", font=pf)
        
        elif event == 'TTS':
            talk(values['in'])
        
        elif event == 'TTS::2':
            talk(values['out'])
            
            
            
        
        
except Exception as e:
    print(e)