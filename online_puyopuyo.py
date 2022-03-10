from flask import *  
from flask_socketio import *

# 非同期処理に使用するライブラリの指定
# `threading`, `eventlet`, `gevent`から選択可能
#async_mode = None

# Flaskオブジェクトを生成し、セッション情報暗号化のキーを指定
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

# Flaskオブジェクト、async_modeを指定して、SocketIOサーバオブジェクトを生成
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('my event', namespace='/test')
def test_connect(data):
    emit('my response', data, broadcast=True)

@socketio.on('ojama', namespace='/test')
def ojama(data):
    emit('ojama', data, broadcast=True)
    
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5004)
