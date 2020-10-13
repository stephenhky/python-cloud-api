import serverless_sdk
sdk = serverless_sdk.SDK(
    org_id='stephenhky',
    application_name='aws-kwan-financial-portfolio',
    app_uid='Z8jLp1lXjKy61CP1DX',
    org_uid='KbkkmHmk3WWZ8kHRT6',
    deployment_uid='74cac4a3-9dca-4779-b87c-1d5db1dc7495',
    service_name='aws-kwan-financial-portfolio',
    should_log_meta=True,
    should_compress_logs=True,
    disable_aws_spans=False,
    disable_http_spans=False,
    stage_name='dev',
    plugin_version='4.0.4',
    disable_frameworks_instrumentation=False
)
handler_wrapper_kwargs = {'function_name': 'aws-kwan-financial-portfolio-dev-finport', 'timeout': 6}
try:
    user_handler = serverless_sdk.get_user_handler('finport.get_optimized_portfolio')
    handler = sdk.handler(user_handler, **handler_wrapper_kwargs)
except Exception as error:
    e = error
    def error_handler(event, context):
        raise e
    handler = sdk.handler(error_handler, **handler_wrapper_kwargs)
