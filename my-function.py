
def lambda_handler(event, context):
    # TODO implement
    if('queryStringParameters' in event and 'keyword' in event['queryStringParameters']):
        statusCode = 200
        message = "Juan Brown Says " + event['queryStringParameters']['keyword']
    else:
        statusCode = 400
        message = "Error no keyword"
    
    return {
        'statusCode': statusCode,
        'body': message
    }
    

    

