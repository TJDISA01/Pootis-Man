from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "You found the legendary Pootis Sandvich! Say and enjoy the friendly vibes, or leave with joy."

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()