import boto3

dbclient = boto3.client('dynamodb')
response = dbclient.execute_statement(Statement="select * from modulos where ciclo='DAW'")
print(response)