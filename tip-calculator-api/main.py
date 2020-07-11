
import request
from flask import Flask, jsonify, request


app = Flask(__name__)


taxrates = {'MD': 0.06, 'VA': 0.06, 'DC': 0.10}


def calculate_tips(subtotal, state, tippercent=0.15, split=1):
    if state not in ('MD', 'VA', 'DC'):
        state = 'MD'
    tax = subtotal * taxrates[state]
    tips = subtotal * tippercent
    total = subtotal + tax + tips
    onesplit = total / split

    return {'subtotal': subtotal, 'state': state,
            'tax': tax, 'tips': tips, 'split': split,
            'total': total, 'onesplit': onesplit}


@app.route('/tipcalculator',methods=['GET'])
def get_tips():
    data = request.get_json(force=True)
    subtotal = data['subtotal']
    state = data['state']
    tippercent = data.get('tippercent', 0.15)
    split = data.get('split', 1)

    result = calculate_tips(subtotal, state, tippercent=tippercent, split=split)
    return jsonify(result)


if __name__ == '__main__':
	app.run(debug=True)