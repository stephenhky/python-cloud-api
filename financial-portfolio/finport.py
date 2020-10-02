
from datetime import datetime, timedelta
import traceback

from finsim.portfolio import get_optimized_portfolio


def get_optimized_portfolio(event, context):
    input_parameters = event['body']
    rf = input_parameters.get('rf', 0.)
    symbols = input_parameters.get('symbols', [])
    totalworth = input_parameters.get('totalworth', 1000.0)
    presetdate = input_parameters.get(
        'presetdate',
        datetime.today().strftime('%Y-%m-%d')
    )
    estimating_startdate = input_parameters.get(
        'estimating_startdate',
        (datetime.today() - timedelta(90)).strftime('%Y-%m-%d')
    )
    estimating_enddate = input_parameters.get(
        'estimating_enddate',
        (datetime.today() - timedelta(1)).strftime('%Y-%m-%d')
    )
    minweight = input_parameters.get('minweight', 0.)
    lazy = input_parameters.get('lazy', False)

    try:
        optimized_portfolio = get_optimized_portfolio(
            rf,
            symbols,
            totalworth,
            presetdate,
            estimating_startdate,
            estimating_enddate,
            minweight,
            lazy=lazy
        )
        response_json = {
            'summary': optimized_portfolio.summary,
            'input_parameters': {
                'rf': rf,
                'symbols': symbols,
                'totalworth': totalworth,
                'presetdate': presetdate,
                'estimating_startdate': estimating_startdate,
                'estimating_enddate': estimating_enddate,
                'minweight': minweight,
                'lazy': lazy
            },
            'input_event': event,
            'input_context': context,
            'statusCode': 200
        }
    except Exception:
        tb = traceback.format_exc()
        response_json = {
            'statusCode': 500,
            'stacktrace': tb,
            'input_event': event,
            'input_context': context
        }

    return response_json
