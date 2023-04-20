import boto3
from botocore.exceptions import ClientError
import sys

#HeadBucket sólo está disponible en la API de bajo nivel de S3
def existeS3Bucket(nombreBucket,region):
    try:
        client = boto3.client('s3')
        client.head_bucket(Bucket=nombreBucket)
        respuesta = 'El bucket existe'
    except ClientError as e:
        match e.response['Error']['Code']:
            case '404':
                respuesta = 'El bucket '+nombreBucket+' no existe'
            case '403':
                respuesta = 'No se tienen permisos para acceder al bucket '+nombreBucket
            case _:
                respuesta = 'Error de cliente'
    finally:
        return respuesta

if len(sys.argv)!= 3:
    print('Uso: head-bucket <nombre-bucket> <region>')
else:    
    respuesta = existeS3Bucket(sys.argv[1],sys.argv[2])
    print(respuesta)