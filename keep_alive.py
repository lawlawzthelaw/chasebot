from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Discord Bot Status</title>
        <style>
            body { font-family: Arial; text-align: center; padding: 50px; }
            .status { color: #00ff00; font-size: 24px; }
        </style>
    </head>
    <body>
        <h1>🤖 Discord Bot</h1>
        <p class="status">¡Estoy vivo!</p>
        <p>Bot está funcionando correctamente</p>
    </body>
    </html>
    '''

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
