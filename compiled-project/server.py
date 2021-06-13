from flask import Flask,render_template,redirect, url_for,request,session,app
from datetime import timedelta
from flask_socketio import SocketIO,send,emit
import _thread
import time

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/2fa')
def twofactorauth():
    return render_template('2fa.html')




@app.route('/test')
def test():
    return render_template('addserver.html')

if __name__ == '__main__':
    socketio.run(app,debug=True)