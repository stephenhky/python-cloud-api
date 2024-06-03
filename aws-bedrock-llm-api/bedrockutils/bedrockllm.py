
import json

import boto3
from langchain.llms.bedrock import Bedrock
from langchain.chains import LLMChain
from botocore.config import Config



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


def get_langchain_bedrock_llm(model_id, client, *args, **kwargs):
    return Bedrock(model_id=model_id, client=client, *args, **kwargs)
