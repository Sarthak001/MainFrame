from flask import Flask,render_template,redirect, url_for,request,session,app
from datetime import timedelta
from flask_socketio import SocketIO,send,emit
import _thread
import time

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/test')
def test():
    return render_template('secured.html')

@app.route('/testing',methods=["POST"])
def testing():
    message = request.form[""]

# @app.route('/test1')
# def test1():
#     return render_template('login.html')

# @app.route('/test2')
# def test2():
#     return render_template('profile.html')

# @app.route('/test3')
# def test3():
#     return render_template('panel.html')

# @app.route('/test4')
# def test4():
#     return render_template('svinfo.html')





if __name__ == '__main__':
    socketio.run(app,debug=True)