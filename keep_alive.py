from flask import Flask
from threading import Thread

app = Flask('neck hurt')

@app.route('/')
def home():
    return "Bot dang chay!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()