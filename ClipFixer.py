import clipboard
from asyncio.windows_events import NULL
#from curses import window
from tkinter import *
from tkinter import ttk
import pyautogui as pya
import tkinter
import time
# import clipboard_handler
# from clipboard_handler import clipF

from pynput.keyboard import Controller
keyboard = Controller()


hedict = {
    'q': '/',
    'a': 'ש',
    'z': 'ז',
    'w': '\'',
    's': 'ד',
    'x': 'ס',
    'e': 'ק',
    'd': 'ג',
    'c': 'ב',
    'r': 'ר',
    'f': 'כ',
    'v': 'ה',
    't': 'א',
    'g': 'ע',
    'b': 'נ',
    'y': 'ט',
    'h': 'י',
    'n': 'מ',
    'u': 'ו',
    'j': 'ח',
    'm': 'צ',
    'i': 'ן',
    'k': 'ל',
    ',': 'ת',
    'o': 'ם',
    'l': 'ך',
    '.': 'ץ',
    'p': 'פ',
    ';': 'ף',
    '/': '.',
    ' ': ' ',
    'Q': '/',
    'A': 'ש',
    'Z': 'ז',
    'W': '\'',
    'S': 'ד',
    'X': 'ס',
    'E': 'ק',
    'D': 'ג',
    'C': 'ב',
    'R': 'ר',
    'F': 'כ',
    'V': 'ה',
    'T': 'א',
    'G': 'ע',
    'B': 'נ',
    'Y': 'ט',
    'H': 'י',
    'N': 'מ',
    'U': 'ו',
    'J': 'ח',
    'M': 'צ',
    'I': 'ן',
    'K': 'ל',
    'O': 'ם',
    'L': 'ך',
    'P': 'פ',

    '/': 'q',
    'ש': 'a',
    'ז': 'z',
    '\\': 'w',
    'ד': 's',
    'ס': 'x',
    'ק': 'e',
    'ג': 'd',
    'ב': 'c',
    'ר': 'r',
    'כ': 'f',
    'ה': 'v',
    'א': 't',
    'ע': 'g',
    'נ': 'b',
    'ט': 'y',
    'י': 'h',
    'מ': 'n',
    'ו': 'u',
    'ח': 'j',
    'צ': 'm',
    'ן': 'i',
    'ל': 'k',
    'ת': ',',
    'ם': 'o',
    'ך': 'l',
    'ץ': '.',
    'פ': 'p',
    'ף': ';',
    '.': '/'
}


class clipF:
    def __init__(self):
        pass

    def get_copied_text(self):
        selected = clipboard.paste()
        return selected
    

    def fix_clipboard(self):
        fixed_text = self.get_fixed_clipboard()
        clipboard.copy(fixed_text)
        pya.hotkey('ctrl', 'v')
        return fixed_text

    def hebrew_english(self, current_clipboard):

        fixed_clipboard = ''
        for i in current_clipboard:
            try:
                fixed_clipboard += hedict[i]
            except:
                continue

        return fixed_clipboard

    # def fix_clipboard(self, window):
    #     fixed_clipboard = self.get_fixed_clipboard()
    #     window.close_window()
    #     keyboard.type(fixed_clipboard)


    def get_fixed_clipboard(self):
        selected_text = self.get_copied_text()
        return self.hebrew_english(selected_text)
        


#tbh rumv krtu, t, zv cgcrh,
#אני רוצה לראות את זה בעברית
