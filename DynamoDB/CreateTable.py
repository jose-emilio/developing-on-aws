import boto3

dynamodb = boto3.resource('dynamodb')

tabla = dynamodb.create_table(
    TableName='modulos',
    KeySchema=[
        {
            'AttributeName': 'ciclo',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'modulo',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'ciclo',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'modulo',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 3,
        'WriteCapacityUnits': 3
    }
)

print("Estado de la tabla:", tabla.table_status)
dynamodb2 =  dynamodb.meta.client
waiter = dynamodb2.get_waiter('table_exists')
waiter.wait(TableName='modulos')
print("Tabla creada")