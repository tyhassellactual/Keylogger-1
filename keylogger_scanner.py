import psutil
import re
import logging
import tkinter as tk
from tkinter import scrolledtext

# Configure logging
logging.basicConfig(filename='detections.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Function to scan for potential keyloggers
def scan_processes():
    keylogger_patterns = [
        re.compile(r'keylogger', re.IGNORECASE),
        re.compile(r'capture', re.IGNORECASE),
        # Add more patterns as needed
    ]

    detections = []
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        try:
            process_info = proc.info
            for pattern in keylogger_patterns:
                if pattern.search(process_info['name']) or pattern.search(process_info['exe']):
                    detection_message = f"Potential keylogger detected: PID={process_info['pid']}, Name={process_info['name']}"
                    detections.append(detection_message)
                    logging.info(detection_message)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return detections

# Function to update the GUI with detections
def update_gui():
    detections = scan_processes()
    for detection in detections:
        text_area.insert(tk.END, detection + '\n')
    text_area.yview(tk.END)
    root.after(10000, update_gui)  # Update GUI every 10 seconds

# GUI Setup
root = tk.Tk()
root.title("Keylogger Detection Tool")

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, font=("Times New Roman", 12))
text_area.pack(padx=10, pady=10)

root.after(1000, update_gui)  # Start updating GUI after 1 second
root.mainloop()
