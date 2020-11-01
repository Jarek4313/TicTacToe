import keyboard

def input_from_user():
    while True:
        if keyboard.is_pressed('down'):
                #print('down is pressed')
            return 1
        elif keyboard.is_pressed('up'):
                #print('down is pressed')
            return -1
        elif keyboard.is_pressed('left'):
            return 100