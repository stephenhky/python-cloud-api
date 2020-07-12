
# Deploy a Flask App on AWS EC2: https://www.codementor.io/@jqn/deploy-a-flask-app-on-aws-ec2-13hp1ilqy2
# Example: https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80

# Keras example
# Article 1: https://towardsdatascience.com/deploying-a-keras-deep-learning-model-as-a-web-application-in-p-fc0f2354a7ff
# Article 2: https://towardsdatascience.com/deploying-a-python-web-app-on-aws-57ed772b2319

# Security: https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https

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