

from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/get/<number>')
def fixed_monthly_payment(L, r, n):
    return L * (r*(1+r)*n) / ((1+r)*n - 1)


if __name__ == '__main__':
	app.run(debug=True)