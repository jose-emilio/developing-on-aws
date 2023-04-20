import boto3
import sys
import json

dynamodb = boto3.client('dynamodb')
respuesta = dynamodb.scan(
    TableName='modulos',
    Select='ALL_ATTRIBUTES',
    Limit=20,
    FilterExpression = "#curso = :curso",
    ExpressionAttributeNames = {
        "#curso":"curso"
    },
    ExpressionAttributeValues = {
        ":curso": { "S": sys.argv[1] }
    },
    ReturnConsumedCapacity='TOTAL',
)

print(json.dumps(respuesta,indent=2))