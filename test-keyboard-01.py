from pynput import keyboard

def on_press(key):
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    print ("(%s)" % k)
    if key == keyboard.Key.esc:
        return False  # stop listener
    #if k in ['1', '2', 'left', 'right']:  # keys of interest
        # self.keys.append(k)  # store it in global-like variable
    #    print('Key pressed: ' + k)
    #    return False  # stop listener; remove this if want more keys

listener = keyboard.Listener(on_press=on_press)
print ('press any password key:')
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys