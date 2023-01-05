from flask import Flask
from utils import format_text


app = Flask(__name__)


@app.route('/')
def index():
    with open('requirements.txt', 'r') as file:
        txt = file.readlines()
    return format_text(txt)


app.run(debug=True, port=12345)
