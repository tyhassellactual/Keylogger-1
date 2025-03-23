#!/bin/bash

# Function to install Python dependencies
install_dependencies() {
    echo "Installing dependencies..."
    pip install -r requirements.txt
}

# Function to run the keylogger
run_keylogger() {
    echo "Running keylogger..."
    python keylogger.py &
    echo "Keylogger is running in the background."
}

# Function to run the keylogger scanner
run_keylogger_scanner() {
    echo "Running keylogger scanner..."
    python keylogger_scanner.py
}

# Main script execution
install_dependencies
run_keylogger
run_keylogger_scanner
