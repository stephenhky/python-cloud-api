
import json


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


def lambda_handler(event, context):
    query = json.loads(event['body'])
    subtotal = query['subtotal']
    state = query['state']
    tippercent = query.get('tippercent', 0.15)
    split = query.get('split', 1)

    calculation_result = calculate_tips(subtotal, state, tippercent=tippercent, split=split)
    event['result'] = json.dumps(calculation_result)
    req_res = {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(event)
    }
    return req_res


# curl command to run this:
# curl --location --request GET 'https://1j79chd1w8.execute-api.us-east-1.amazonaws.com/default/Ingram1623TipCalculator' \
# --header 'Content-Type: application/json' \
# --data-raw '{"subtotal": 100, "state": "MD", "split": 2}'