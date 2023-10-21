import PySimpleGUI as sg

colaVanilla = './button_images/colaVanilla.png'
no_titleBar = False
fullscreen = False

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Button(image_source=colaVanilla, key='Ok1', button_color=sg.theme_background_color(), border_width=0)],
            [sg.Button(image_source=colaVanilla, key='Ok2', button_color=sg.theme_background_color(), border_width=0)] ]

layout1 = [  [sg.Button(image_source=colaVanilla, key='Ok1', button_color=sg.theme_background_color(), border_width=0)]]


# Create the Window
window = sg.Window('Window Title', layout, finalize=True, no_titlebar=no_titleBar)
window.set_min_size([800, 480])
# Event Loop to process "events" and get the "values" of the inputs

if fullscreen:
    window.maximize()



while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Ok2':  # if user closes window or clicks cancel
        break
    if event == 'Ok1':
        print(event, values)

window.close()
