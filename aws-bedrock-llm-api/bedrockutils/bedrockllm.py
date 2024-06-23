
import json

import boto3


def get_bedrock_runtime(region_name, *args, **kwargs):
    return boto3.client(service_name='bedrock-runtime', region_name=region_name, *args, **kwargs)


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

