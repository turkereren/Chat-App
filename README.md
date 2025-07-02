# Real-Time Chat Application

A simple and modern real-time chat app built with Flask and Flask-SocketIO on the backend, and Socket.IO-client on the frontend. Uses Python’s threading model, so no extra async libraries are required.

---

## 📦 Features

- **Real-Time**: WebSocket-based messaging  
- **Threading**: Uses Python’s built-in threading for concurrency  
- **Modern UI**: Card layout, Google Font (Roboto), CSS variables  
- **Enter Key Support**: Press Enter to join or send messages  
- **Easy Deployment**: Ready for Docker or Heroku  

---

## 🚀 Getting Started

Follow these steps to run the project locally.

### Prerequisites

- Python 3.7+  
- Git  
- (Optional) Docker  

### Installation

```bash
# 1. Clone this repository
git clone https://github.com/<your-username>/chat-app.git
cd chat-app

# 2. Create a virtual environment
# Windows:
py -3 -m venv venv
# macOS/Linux:
python3 -m venv venv

# 3. Activate the virtual environment
# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# Windows (CMD):
venv\Scripts\activate.bat
# macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

🤝 Contributing
Fork this repository

Create a new branch (git checkout -b feature/your-feature)

Commit your changes (git commit -m 'Add some feature')

Push to the branch (git push origin feature/your-feature)

Open a Pull Request
