from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def home():
    return "I'm alive"

def run():
    app.run(host='0.0.0.0', port = 8000)
def keep_alive():
    server = Thread(target=run)
    server.start()    