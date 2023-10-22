import PySimpleGUI as sg

colaVanilla = './button_images/colaVanilla.png'
backArrow = './button_images/backArrow.png'
no_titleBar = False
fullscreen = False

def collapse(layout, key):
    """
    Helper function that creates a Column that can be later made hidden, thus appearing "collapsed"
    :param layout: The layout for the section
    :param key: Key used to make this seciton visible / invisible
    :return: A pinned column that can be placed directly into your layout
    :rtype: sg.pin
    """
    return sg.pin(sg.Column(layout, key=key), shrink=True)

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.


column_home = [
    [sg.Button(image_source=colaVanilla, key='0', image_size=(200, 200)),
             sg.Button(image_source=colaVanilla, key='1', image_size=(200, 200)),
             sg.Button(image_source=colaVanilla, key='2', image_size=(200, 200))],
    [sg.Button(image_source=colaVanilla, key='3', image_size=(200, 200))]
]

column_product = [
    [sg.T('ASD')],
    [sg.Button(image_source=backArrow, key='backArrow', enable_events=True)]
]

layout = [[collapse(column_home, key='home'), collapse(column_product, 'product')]]


# Create the Window
window = sg.Window('Window Title', layout, no_titlebar=no_titleBar)
#window.set_min_size([800, 480])
#window.move_to_center()


# Event Loop to process "events" and get the "values" of the inputs

if fullscreen:
    window.maximize()

home = [window['0'], window['1'], window['2'], window['3']]

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
        break
    if event == '0':
        for e in home:
            print("ASD")
            e.update(visible=False)
        window['product'].update(visible=True)

    if event == 'backArrow':
        for e in home:
            print("ASD")
            e.update(visible=True)
        window['product'].update(visible=False)


window.close()