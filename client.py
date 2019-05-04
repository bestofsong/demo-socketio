import time
import socketio
PORT=5000
HOST = 'http://localhost:%d' % PORT
nsp = '/demo'

# standard Python
sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('I\'m connected!')

@sio.on('message')
def on_message(data):
    print('I received a message!')

@sio.on('my message')
def on_custom_message(data):
    print('I received a custom message!')

@sio.on('disconnect')
def on_disconnect():
    print('I\'m disconnected!')

sio.connect(HOST, namespaces=[nsp])

def my_message_cb(*args):
    for arg in args:
        print('my_message_cb arg: %s' % (arg))

time.sleep(1)
sio.emit(
        'my message',
        data={'foo': 'bar'},
        callback=my_message_cb,
        namespace=nsp)
sio.wait()
