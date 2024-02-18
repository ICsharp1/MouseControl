import keyboard

def get_key_combination():

    combination = []

    while True:
        event = keyboard.read_event(suppress=True)
        
        # Map left and right modifier keys to their general counterparts
        if event.name == 'left windows':
            event.name = 'cmd'
        elif event.name == 'right shift':
            event.name = 'shift'
        elif "ctrl" in event.name:
            event.name = 'ctrl'
        elif event.name == 'right alt':
            event.name = 'alt'
        
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'esc':
                break
            if event.name not in combination:
                combination.append(event.name)
        elif event.event_type == keyboard.KEY_UP:
            break

    return combination

if __name__ == "__main__":
    combination = get_key_combination()
    print("Your key combination:", "+".join(combination))
