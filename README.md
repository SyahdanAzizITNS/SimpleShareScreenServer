**Screen Sharing Application**
This project is a simple screen-sharing application that allows you to share your screen over a local network without requiring an internet connection. The server captures the screen from the host computer and transmits it to the client computers within the same local network. The client computers display the shared screen in real-time.

Technologies Used
- Python: For the server-side application.
- Flask: A lightweight WSGI web application framework for Python.
- Flask-SocketIO: For WebSocket communication between the server and clients.
- PyAutoGUI: For capturing screenshots.
- Pillow: For image processing.
- HTML5: For the client-side interface.
- JavaScript: For handling WebSocket communication and rendering the screen on the client side.

**How It Works**

**Server Side**
The server captures the screen at regular intervals and sends the screenshots to the connected clients via WebSocket. The Flask-SocketIO library is used for real-time communication.

**Client Side**
The client side is an HTML page that connects to the server via WebSocket, receives the screenshots, and displays them on a canvas element. The canvas is dynamically resized to fit the window, making the application responsive.

**How to Run**
**Install Dependencies:**
1. Ensure you have Python installed.
2. Install required Python libraries:
3. pip install flask flask-socketio pyautogui pillow

**Run the Server:**
1. Save the server code in a file named server.py.
2. Save the client code in a file named index.html in the same directory as server.py.

python server.py

**Access the Client:**
1. Open a web browser on a client computer within the same local network.
2. Navigate to the server's IP address and port (e.g., http://192.168.1.10:5000).

**Features**
1. Real-time screen sharing over a local network.
2. Responsive client-side interface that adapts to the size of the window.
3. Easy to set up and run without requiring internet access.
4. Future Improvements
5. Add authentication to secure the screen sharing.
6. Implement better image compression to improve performance.
7. Add the ability to control the host computer from the client side.
