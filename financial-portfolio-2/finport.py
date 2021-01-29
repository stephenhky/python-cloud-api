
import json
from finsim.portfolio.create import get_optimized_portfolio_on_mpt_entropy_costfunction


def portfolio_handler(event, context):
    # getting query
    query = json.loads(event['body'])

    # getting parameter
    rf = query['rf']
    symbols = query['symbols']
    totalworth = query['totalworth']
    presetdate = query['presetdate']
    estimating_startdate = query['estimating_startdate']
    estimating_enddate = query['estimating_enddate']
    riskcoef = query.get('riskcoef', 0.3)
    homogencoef = query.get('homogencoef', 0.1)
    V = query('V', 10.0)

    optimized_portfolio = get_optimized_portfolio_on_mpt_entropy_costfunction(
        rf,
        symbols,
        totalworth,
        presetdate,
        estimating_startdate,
        estimating_enddate,
        riskcoef,
        homogencoef,
        V=V,
        lazy=False
    )

    req_res = {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(event),
        'portfolio': optimized_portfolio.portfolio_summary
    }
    return req_res
