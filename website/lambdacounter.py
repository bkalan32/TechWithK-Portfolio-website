import json
import boto3
from decimal import Decimal

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('visitorcounter')

    try:
        # Get the current views count
        response = table.get_item(Key={'ID': '0'})
        current_views = response.get('Item', {}).get('views', 0)

        # Increment the views count
        new_views = current_views + 1

        # Update the DynamoDB item with the new views count
        response = table.put_item(Item={'ID': '0', 'views': new_views})

        # Convert Decimal to int for JSON serialization
        response_body = {
            'statusCode': 200,
            'body': json.dumps({'views': int(new_views)}, cls=DecimalEncoder)
        }

        return response_body

    except Exception as e:
        # Handle exceptions, log them, or return an error response
        error_body = {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}, cls=DecimalEncoder)
        }

        return error_body

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return int(o)
        return super(DecimalEncoder, self).default(o)

        error_body = {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}, cls=DecimalEncoder)
        }

        return error_body

        return error_body
