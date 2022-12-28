from googletrans import Translator
import PySimpleGUI as sg
import images
import pyperclip
import winshell, os, win32com.client





iconlol = images.icon
desk = winshell.desktop()


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
    tf = 'Arial ', 12, 'bold', 'underline'
    theme = sg.theme('DarkGrey9')



    layout = [
            [sg.Combo(['English', 'French','Spanish','Arabic', 'Dutch', 'Japanese', 'Russian', 'Serbian', 'Romanian', 'Bosnian', 'Finnish', 'Italian'], font=f, key='langin', auto_size_text=True), sg.Combo(['English', 'French','Spanish','Arabic', 'Dutch', 'Japanese', 'Russian', 'Serbian', 'Romanian', 'Bosnian', 'Finnish', 'Italian'], font=f, key='langout', pad=(283, 0))],
            [sg.Multiline('Translation Input',key='in', size=(40, 15), font=f, no_scrollbar=True, right_click_menu=['&Right', ['&Copy All', '---', '&Paste', '---', '&Swap::1']]), sg.Button('Translate', key='butt'), sg.Multiline('Translation Output', key='out', size=(40, 15 ), font=f, no_scrollbar=True, right_click_menu=['&Right',['&Copy All::copy2','---', 'Paste::2', '&Swap::1']])],
            [sg.Button('<-->', key='invert', pad=(309,10), size=(5,1), font=f)]
            ]
            

    window = sg.Window('Translator', layout, use_custom_titlebar=True, titlebar_font=tf, resizable=False, titlebar_background_color='Gray', titlebar_icon=iconlol, titlebar_text_color='white')

    while True:
        event, values = window.read()
        
        
        if event == sg.WIN_CLOSED:
            break
        
        if event == 'butt':
            try:
                trans = Translator()
                translations = trans.translate(values['in'], dest=values['langout'], src=values['langin'])
                window['out'].update(translations.text)
            except Exception as e:
                print(e)
                sg.popup_error('Invalid Source Language', font=f)
        
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
        
        
except Exception as e:
    print(e)
    