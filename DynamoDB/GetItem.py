import boto3
import sys
import json

dynamodb = boto3.resource('dynamodb')
tabla = dynamodb.Table('modulos')
respuesta = tabla.get_item(
    Key={
        'modulo': sys.argv[1],
        'ciclo': sys.argv[2]
    },
    ReturnConsumedCapacity='TOTAL',
    ConsistentRead=True
)

print(json.dumps(respuesta,indent=2))