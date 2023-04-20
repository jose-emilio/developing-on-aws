import boto3
import json
import sys

dynamodb = boto3.resource('dynamodb')
tabla = dynamodb.Table('modulos')
respuesta = tabla.delete_item(
    Key={
        "ciclo": sys.argv[1],
        "modulo": sys.argv[2]
    },
    ReturnValues='ALL_OLD',
    ReturnConsumedCapacity='TOTAL'
)

print(json.dumps(respuesta,indent=2))
