import json

def lambda_handler(event, context):
    query = event.get("query")
    return {
        'statusCode': 200,
        'body': json.dumps(f"Lambda processed query: {query}")
    }
