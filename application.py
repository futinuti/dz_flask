from flask import Flask, render_template
from utils import get_avr_data, set_kg, set_sm


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Index page', content='из файла hw.csv')


@app.route('/avr_data')
def avr_data():
    with open('hw.csv', 'rt') as f:
        f = f.readlines()
        weight = set_kg(get_avr_data(f)[0])
        height = set_sm(get_avr_data(f)[1])
    return render_template('avr_data.html', title='avr_data', weight=weight, height=height)


app.run(debug=True, port=12345)


