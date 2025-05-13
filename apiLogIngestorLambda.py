import json
import boto3
import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('LogMetadataTable')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        log_id = body['log_id']
        source = body.get('source', 'api')

        timestamp = str(datetime.datetime.now())

        table.put_item(
            Item={
                'log_id': log_id,
                'timestamp': timestamp,
                'source': source,
                'status': 'Processed via API'
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Log entry processed successfully'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
