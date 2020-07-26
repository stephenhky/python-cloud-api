

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
    subtotal = event['subtotal']
    state = event['state']
    tippercent = event.get('tippercent', 0.15)
    split = event.get('split', 1)

    calculation_result = calculate_tips(subtotal, state, tippercent=tippercent, split=split)
    return calculation_result
