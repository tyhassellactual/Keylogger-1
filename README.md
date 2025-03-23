# Keylogger Detection Tool

## Overview
This project includes two main scripts:
1. `keylogger.py`: A keylogger that installs dependencies and logs keystrokes.
2. `keylogger_scanner.py`: A scanner that checks for keyloggers running in the background and includes a front-end interactive GUI.

**Note**: Please ensure you have explicit permission from the user before running any keylogging software. Unauthorized use of keyloggers is illegal and unethical.

## Prerequisites
- Python 3 installed on the system.
- Required Python libraries:
  - `psutil`
  - `pynput`
  - `tkinter`

## Installation and Usage

### 1. Keylogger (keylogger.py)
This script installs the necessary dependencies and logs keystrokes in the background.

#### Steps:
1. **Save the Script**: Save the script as `keylogger.py`.
2. **Run the Script**:
   ```sh
   python keylogger.py
   ```
3. **Background Execution**: To run the script in the background:
   - **Windows**:
     ```sh
     start /B python keylogger.py
     ```
   - **macOS and Linux**:
     ```sh
     nohup python keylogger.py &
     ```

The keystrokes will be logged to `keylogger.log` in the same directory as the script.

### 2. Keylogger Scanner (keylogger_scanner.py)
This script scans for potential keyloggers running in the background and displays the results in a GUI.

#### Steps:
1. **Save the Script**: Save the script as `keylogger_scanner.py`.
2. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the Script**:
   ```sh
   python keylogger_scanner.py
   ```

This will open the GUI and start scanning for potential keyloggers in the background. The detections will be displayed in the GUI and logged to `detections.log`.

### 3. Run Using Bash Script (run_keylogger.sh)
This script installs the dependencies, runs the keylogger in the background, and starts the keylogger scanner with the GUI.

#### Steps:
1. **Make the Script Executable**:
   ```sh
   chmod +x run_keylogger.sh
   ```
2. **Run the Script**:
   ```sh
   ./run_keylogger.sh
   ```

## Dependencies
List the following dependencies in your `requirements.txt`:
```text
psutil
pynput
tkinter
```

## Ethical Use
Ensure you have explicit permission from the user before running any keylogging software. Unauthorized use of keyloggers is illegal and unethical. Be aware of the legal implications and ensure compliance with local laws and regulations.
