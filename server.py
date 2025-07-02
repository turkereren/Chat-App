from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'replace-with-your-secret'


socketio = SocketIO(
    app,
    cors_allowed_origins="*",
    async_mode='threading',
    logger=True,
    engineio_logger=True
)


users = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print(f"[CONNECT] {request.sid}")

@socketio.on('disconnect')
def handle_disconnect():
    username = users.pop(request.sid, None)
    if username:
        emit('user_left', {'msg': f"{username} ayrıldı."}, broadcast=True)
    print(f"[DISCONNECT] {request.sid}")

@socketio.on('join')
def handle_join(data):
    username = data.get('username', 'Anonim')
    room = data.get('room', 'main')
    users[request.sid] = username
    join_room(room)
    emit('user_joined', {'msg': f"{username} katıldı."}, room=room)
    print(f"[JOIN] {username} in room {room}")

@socketio.on('message')
def handle_message(data):
    room = data.get('room', 'main')
    username = users.get(request.sid, 'Anonim')
    msg = data.get('msg', '')
    emit('message', {'username': username, 'msg': msg}, room=room)
    print(f"[MSG] {username}@{room}: {msg}")

if __name__ == '__main__':

    socketio.run(app, host='0.0.0.0', port=5000)
