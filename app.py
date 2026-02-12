# Коментарі українською 😉

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def index():
    return render_template("index.html")

# передаємо всі сигнали іншому користувачу
@socketio.on("signal")
def handle_signal(data):
    emit("signal", data, broadcast=True, include_self=False)

if __name__ == "__main__":
    socketio.run(app)
