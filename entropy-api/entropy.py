
import numpy as np
import json


def entropy(probs):
    norm_probs = np.array(probs)/np.sum(probs)
    entropy = sum(-norm_probs*np.log(norm_probs))
    return entropy


def hello_world(request):
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        query = request_json['query']
        results = entropy(query)
        return json.dumps(results)
