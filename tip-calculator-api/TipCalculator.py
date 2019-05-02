import json

taxrates = {'MD': 0.06, 'VA': 0.06, 'DC': 0.10}


def calculate_tips(subtotal, state, tippercent=0.15, split=1):
    if state not in ('MD', 'VA', 'DC'):
        state = 'MD'
    tax = subtotal * (1+taxrates[state])
    tips = subtotal * (1+tippercent)
    total = subtotal + tax + tips
    onesplit = total / split

    return {'subtotal': subtotal, 'state': state,
            'tax': tax, 'tips': tips, 'split': split,
            'total': total, 'onesplit': onesplit}


def hello_world(request):
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        query = request_json['query']
        results = calculate_tips(query['subtotal'],
                                 query.get('state', 'MD'),
                                 query.get('tippercent', 0.15),
                                 query.get('split', 1))
        return json.dumps(results)


# test case: {"query": {"subtotal": 10, "state": "MD"}}
