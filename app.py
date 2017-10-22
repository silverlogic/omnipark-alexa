import os

from flask import Flask
from flask_ask import Ask, statement, question, session

import requests

app = Flask(__name__)
ask = Ask(app, '/')


@ask.intent('ReserveParkingIntent')
def reserve_parking(merchant):
    return statement('I have reserved a spot for you.')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
