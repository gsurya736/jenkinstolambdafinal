import json

def lambda_handler(event, context):
    # TODO implement test2 final current
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda test with git hub test!')
    }
