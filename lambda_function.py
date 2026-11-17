import json
import uuid
from datetime import datetime, timezone
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ContactSubmissions')

def lambda_handler(event, context):
  try:
    # Parse incoming JSON body from API Gateway
    body = json.loads(event.get('body', '{}'))

    name = body.get('name')
    email = body.get('email')
    message = body.get('message')

    # Basic validation
    if not name or not email or not message:
      return {
          'statusCode': 400,
          'headers': {'Access-Control-Allow-Origin': '*'},
          'body': json.dumps({'error': 'All fields are required.'}),
      }

    # Generate unique ID and timestamp
    submission_id = str(uuid.uuid4())
    timestamp = datetime.now(timezone.utc).isoformat()

    # Save item to DynamoDB
    table.put_item(
        Item={
            'SubmissionID': submission_id,
            'Name': name,
            'Email': email,
            'Message': message,
            'SubmittedAt': timestamp,
        }
    )

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS,POST',
        },
        'body': json.dumps(
            {'message': 'Form submitted successfully!', 'id': submission_id}
        ),
    }

  except Exception as e:
    return {
        'statusCode': 500,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps({'error': str(e)}),
    }
