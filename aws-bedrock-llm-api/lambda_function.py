
import json
import logging

import boto3


get_bedrock_runtime = lambda region_name: boto3.client(service_name='bedrock-runtime', region_name=region_name)


def call_bedrock_models(prompt_config, model_id, bedrock_runtime):
    body = json.dumps(prompt_config)

    accept = 'application/json'
    content_type = 'application/json'

    response = bedrock_runtime.invoke_model(
        body=body,
        modelId=model_id,
        accept=accept,
        contentType=content_type
    )
    response_body = json.loads(response.get('body').read())

    results = response_body.get('outputs')[0].get('text')
    return results


def lambda_handler(events, context):
    # get query
    # query = json.loads(events)['body']
    query = events['body']
    logging.info(query)
    print(query)

    # get bedrock runtime
    bedrock_runtime = get_bedrock_runtime('us-east-1')

    # get prompts
    prompt = query['prompt']

    # get model config
    config = query['config']
    model_id = query['model_id']
    body = {'prompt': prompt} | config

    # call model
    results = call_bedrock_models(body, model_id, bedrock_runtime)

    return {
        'statusCode': 200,
        'body': results
    }
