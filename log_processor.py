import json
import boto3
import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('LogMetadataTable')

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        timestamp = str(datetime.datetime.now())

        # Insert metadata into DynamoDB
        response = table.put_item(
            Item={
                'log_id': key,
                'timestamp': timestamp,
                'source': bucket,
                'status': 'Processed'
            }
        )

        print(f"Inserted log metadata for: {key}")

    return {
        'statusCode': 200,
        'body': json.dumps('Log Processed')
    }
