from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO, emit
import eventlet

eventlet.monkey_patch()

app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet')
current_page = 1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pdf/<path:filename>')
def pdf_viewer(filename):
    return send_from_directory('.', filename)

@socketio.on('join')
def handle_join():
    emit('page_update', {'page': current_page})

@socketio.on('change_page')
def handle_change_page(data):
    global current_page
    current_page = data['page']
    emit('page_update', {'page': current_page}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
