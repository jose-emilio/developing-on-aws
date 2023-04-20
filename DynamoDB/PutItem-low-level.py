import boto3
import json

dynamodb = boto3.client('dynamodb')

respuesta = dynamodb.put_item(
    TableName="modulos",
    Item={
        "modulo": {"S": "Desarrollo Web en Entorno Cliente"},
        "ciclo": {"S": "DAW"},
        "curso": {"N": "2"},
        "horas": {"N": "5"}
    }
)

print(json.dumps(respuesta,indent=2))