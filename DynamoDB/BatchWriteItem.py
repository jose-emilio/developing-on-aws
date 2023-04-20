import boto3
import json

dynamodb = boto3.resource('dynamodb')

respuesta = dynamodb.batch_write_item(
    RequestItems={
        'modulos': [
            {
                'PutRequest': {
                    'Item': {
                        'modulo': 'Desarrollo Web en Entorno Servidor',
                        'ciclo': 'DAW',
                        'curso': '2',
                        'horas': '9'
                    }
                }
            },
            {
                'PutRequest': {
                    'Item': {
                        'modulo': 'Entornos de Desarrollo',
                        'ciclo': 'DAW',
                        'curso': '1',
                        'horas': '3'
                    }
                }
            },
            {
                'PutRequest': {
                    'Item': {
                        'modulo': 'Programacion',
                        'ciclo': 'DAW',
                        'curso': '1',
                        'horas': '9'
                    }
                }
            },
            {
                'PutRequest': {
                    'Item': {
                        'modulo': 'Programacion de Servicios y Procesos',
                        'ciclo': 'DAM',
                        'curso': '2',
                        'horas': '4'
                    }
                }
            },
            {
                'PutRequest': {
                    'Item': {
                        'modulo': 'Entornos de Desarrollo',
                        'ciclo': 'DAM',
                        'curso': '1',
                        'horas': '3'
                    }
                }
            },
            {
                'PutRequest': {
                    'Item': {
                        'modulo': 'Seguridad y Alta Disponibilidad',
                        'ciclo': 'ASIR',
                        'curso': '2',
                        'horas': '4'
                    }
                }
            },
            {
                'PutRequest': {
                    'Item': {
                        'modulo': 'Gestion de Bases de Datos',
                        'ciclo': 'ASIR',
                        'curso': '1',
                        'horas': '5'
                    }
                }
            },
            {
                'PutRequest': {
                    'Item': {
                        'modulo': 'Planificacion y Administracion de Redes',
                        'ciclo': 'ASIR',
                        'curso': '1',
                        'horas': '6'
                    }
                }
            }
        ]
    },
    ReturnConsumedCapacity='TOTAL',
    ReturnItemCollectionMetrics='SIZE'
)

print(json.dumps(respuesta,indent=2))