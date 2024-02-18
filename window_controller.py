from window_handler import TransparentWindow
from ClipFixer import clipF

f = clipF()

def fixClipboard():
    f.fix_clipboard()

def add_clip_to_list(copied_text):
    if isinstance(copied_text, str):
        if copied_text:
            with open('clips.txt', 'a', encoding="utf-8") as file:
                file.write(copied_text + '\n')
                file.close()
        else:
            print("Copied text is empty")
    else:
        print("Copied text is not a string")


def add_to_clip_button():
    copied = f.get_copied_text()
    add_clip_to_list(copied)

def temp():
    print('just a really cool button')

def start_window():
    print('trying to open the kite window')
    app = TransparentWindow()
    app.add_button('Fix clipboard', fixClipboard)
    app.add_button('Add clip list', add_to_clip_button)
    app.add_button('One last button', temp)
    app.add_button('Close window', app.close_window)
    app.mainloop()

start_window()