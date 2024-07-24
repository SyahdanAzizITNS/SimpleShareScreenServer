from flask import Flask, send_from_directory
from flask_socketio import SocketIO, emit
import pyautogui
import io
import base64
from PIL import Image

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@socketio.on('request_screenshot')
def handle_request_screenshot():
    screenshot = pyautogui.screenshot()
    buffer = io.BytesIO()
    screenshot.save(buffer, format="JPEG")
    img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
    emit('screenshot', {'image': img_str})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
