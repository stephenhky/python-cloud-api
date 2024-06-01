
import boto3
from langchain.llms.bedrock import Bedrock
from langchain.chains import LLMChain
from botocore.config import Config


retry_config = Config(
    region_name='us-east-1',
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)


def get_bedrock_llm_instance(model_id, model_kwargs):
    session = boto3.session.Session(profile_name='tesdl-ml-beta')
    boto3_bedrock = session.client('bedrock', config=retry_config)
    boto3_bedrock_runtime = session.client('bedrock-runtime', config=retry_config)

    llm = Bedrock(
        model_id=model_id,
        client=boto3_bedrock_runtime,
        model_kwargs=model_kwargs
    )

    return llm
