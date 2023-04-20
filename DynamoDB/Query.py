import boto3
import sys
import json

dynamodb = boto3.client('dynamodb')
respuesta = dynamodb.query(
    TableName='modulos',
    Select='ALL_ATTRIBUTES',
    KeyConditionExpression ='#ciclo = :ciclo',
    FilterExpression = "#curso = :curso",
    ExpressionAttributeNames = {
        "#ciclo":"ciclo",
        "#curso":"curso"
    },
    ExpressionAttributeValues = {
        ":ciclo": { "S": sys.argv[1] },
        ":curso": { "S": sys.argv[2] }
    },
    ReturnConsumedCapacity='TOTAL'
)

print(json.dumps(respuesta,indent=2))