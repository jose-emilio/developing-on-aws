import boto3
import json

dynamodb = boto3.resource('dynamodb')
tabla = dynamodb.Table('modulos')
respuesta = tabla.put_item(
    Item={
        "ciclo": "DAW",
        "modulo": "Despliegue de Aplicaciones Web",
        "curso": "2",
        "horas": "4"
    }
)

print(json.dumps(respuesta,indent=2))