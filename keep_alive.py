from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/healthz')
def health_check():
    return 'me may beo!', 200

@app.route('/')
def home():
    print("Bot song.")
    return "Bot sống và del có lỗi", 200

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()