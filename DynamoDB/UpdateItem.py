import boto3
import json

dynamodb = boto3.resource('dynamodb')
tabla = dynamodb.Table('modulos')
respuesta = tabla.update_item(
    Key={
        "ciclo": "DAW",
        "modulo": "Entornos de Desarrollo"
    },
    AttributeUpdates={
        "horas": {
            "Value": "4",
            "Action": "PUT"
        }
    },
    ReturnValues='ALL_NEW',
    ReturnConsumedCapacity='TOTAL'
)

print(json.dumps(respuesta,indent=2))