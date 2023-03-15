from flask import Flask, request, render_template
from utils import get_currency_exchange_rate, get_pb_exchange_rate
import random
import string
app = Flask(__name__)


@app.route("/rates", methods=['GET'])
def get_rates():
    currency_a = request.args.get('currency_a', default='USD')
    currency_b = request.args.get('currency_b', default='UAH')
    result = get_currency_exchange_rate(currency_a, currency_b)
    return result

@app.route("/login", methods=['GET', 'POST'])
def login_user():
    if request.method == 'GET':
        return render_template('login.html',
                               username='username',
                               age='age',
                               )
    if request.method == 'POST':
        name = request.form['username']
        age = request.form['age']
        generated_password = ''.join(random.choices(string.ascii_letters + string.digits, k=int(age)))
        return f'Hello, {name}! Your password: {generated_password}'

@app.route("/rates_pb", methods=['GET'])
def get_pb_rates():
    convert_currency = request.args.get('convert_currency', default='USD')
    bank = request.args.get('bank', default='NBU')  # TODO додати функцію валідації вводу банку
    rate_date = request.args.get('rate_date', default='01.11.2022')
    result = get_pb_exchange_rate(convert_currency, bank, rate_date)
    return result

if __name__ == '__main__':
    app.run()
