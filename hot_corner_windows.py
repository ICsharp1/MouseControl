import pyautogui
from pynput.keyboard import Key, Controller
import time
import os
from json_handler import load_corner_data

KEY_MAP = {
  "backspace": Key.backspace,
  "tab": Key.tab,
  "enter": Key.enter,
  "shift": Key.shift,
  "ctrl": Key.ctrl,
  "alt": Key.alt,
  "pause": Key.pause,
  "caps_lock": Key.caps_lock,
  "esc": Key.esc,
  "space": Key.space,
  "page_up": Key.page_up,
  "page_down": Key.page_down,
  "end": Key.end,
  "home": Key.home,
  "left": Key.left, 
  "up": Key.up,
  "right": Key.right,
  "down": Key.down,
  "insert": Key.insert,
  "delete": Key.delete,
  "cmd": Key.cmd,
  "win": Key.cmd,
  "print_screen": Key.print_screen,
  "scroll_lock": Key.scroll_lock,

  "f1": Key.f1,
  "f2": Key.f2,
  "f3": Key.f3,
  "f4": Key.f4,
  "f5": Key.f5,
  "f6": Key.f6,
  "f7": Key.f7,
  "f8": Key.f8,
  "f9": Key.f9,
  "f10": Key.f10,
  "f11": Key.f11,
  "f12": Key.f12,

  "a": 'a',
  "b": 'b',
  "c": 'c',
  "d": 'd',
  "e": 'e',
  "f": 'f',
  "g": 'g',
  "h": 'h',
  "i": 'i',
  "j": 'j',
  "k": 'k',
  "l": 'l',
  "m": 'm',
  "n": 'n',
  "o": 'o',
  "p": 'p',
  "q": 'q',
  "r": 'r',
  "s": 's',
  "t": 't',
  "u": 'u',
  "v": 'v',
  "w": 'w',
  "x": 'x',
  "y": 'y',
  "z": 'z',

  "A": 'A',
  "B": 'B',
  "C": 'C',
  "D": 'D',
  "E": 'E',
  "F": 'F',
  "G": 'G',
  "H": 'H',
  "I": 'I',
  "J": 'J',
  "K": 'K',
  "L": 'L',
  "M": 'M',
  "N": 'N',
  "O": 'O',
  "P": 'P',
  "Q": 'Q',
}




def press_keys(keys, keyboard):
    for key in keys:
        key_to_press = KEY_MAP.get(key, None)
        if not key_to_press is None:
            keyboard.press(key_to_press)

    for key in keys:
        key_to_press = KEY_MAP.get(key, None)
        if not key_to_press is None:
            keyboard.release(key_to_press)

def mouse_event(keys, keyboard):
    if keys:
        print(f'pressing {keys}')
        press_keys(keys, keyboard)
    else:
        print('keys was empty')


def PopsDown():
    print('')





filename = 'position-corner.json'
filename = 'test.json'
corner_screens = load_corner_data(filename)
keyboard = Controller()


corners_len = len(corner_screens)
was_in_area = [False]*corners_len
is_in_area = [False]*corners_len
delay_loop = 0.01

def handle_corner_action(corner, keyboard):
    if corner.type == 'shortcut':
        mouse_event(corner.keys, keyboard)
    elif corner.type == 'command':
        os.system(f"python \"{corner.file_to_execute}\"")
        

while True:
    mouse_position = pyautogui.position()
    time.sleep(delay_loop)
    for corner in corner_screens:
        number = corner.number
        was_in_area[number] = is_in_area[number]
        if (corner.left_x <= mouse_position.x <= corner.right_x) and (
                corner.top_y <= mouse_position.y <= corner.bottom_y):
            is_in_area[number] = True
            if not was_in_area[number] and is_in_area[number]:
                handle_corner_action(corner, keyboard)
                time.sleep(0.3)
                
        elif was_in_area[number]:
            #threading.Thread(target=PopsDown).start()
            is_in_area[number] = False
        else:
            is_in_area[number] = False

        # if number == 3:
        #     print(f'\nwas { "" if was_in_area[number] else " not "} in area, and now it is{"" if is_in_area[number] else "nt"}\n')


#nna neuuv azv hgcus
