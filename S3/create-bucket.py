import boto3
from botocore.exceptions import ClientError
import sys

# CrearBucket mediante la API de alto nivel de S3
# Crea un bucket privado
def crearBucketResource(nombreBucket,region):
    try:
        session = boto3.Session(profile_name='lab')
        client = session.resource('s3',region_name=region)
        if region != 'us-east-1':
            bucket = client.create_bucket(
                ACL='private',
                Bucket=nombreBucket,
                CreateBucketConfiguration={
                    'LocationConstraint':region
                }
            )
        else:
           bucket = client.create_bucket(
                ACL='private',
                Bucket=nombreBucket
            ) 
        #Waiter sólo están disponibles en la API de bajo nivel
        #A partir del recurso se puede obtener el cliente de bajo nivel para generar el waiter
        waiter = bucket.meta.client.get_waiter('bucket_exists')
        waiter.wait(Bucket=nombreBucket)
        respuesta = 'El bucket '+nombreBucket+' fue creado con éxito'
    except ClientError as e:
        match e.response['Error']['Code']:
            case 'BucketAlreadyExists':
                respuesta = 'El bucket '+nombreBucket+' ya existe en otra cuenta'
            case 'BucketAlreadyOwnedByYou':
                respuesta = 'El bucket '+nombreBucket+' ya existe en tu cuenta'
            case 'AccessDenied':
                respuesta = 'No se tienen permisos para crear el bucket'
            case _:
                respuesta = 'Error de cliente: '+e.response['Error']['Code']
    finally:
        return respuesta

# CrearBucket mediante la API de bajo nivel de S3
# Crea un bucket privado
def crearBucketClient(nombreBucket,region):
    try:
        session = boto3.Session(profile_name='lab')
        client = session.client('s3')
        if region != 'us-east-1':
            bucket = client.create_bucket(
                ACL='private',
                Bucket=nombreBucket,
                CreateBucketConfiguration={
                    'LocationConstraint':region
                }
            )
        else:
           bucket = client.create_bucket(
                ACL='private',
                Bucket=nombreBucket
            ) 
        #Se espera a que el bucket esté creado
        #Sólo es posible con la API de bajo nivel
        waiter = client.get_waiter('bucket_exists')
        waiter.wait(Bucket=nombreBucket)
        respuesta = 'El bucket '+nombreBucket+' fue creado con éxito'
    except ClientError as e:
        match e.response['Error']['Code']:
            case 'BucketAlreadyExists':
                respuesta = 'El bucket '+nombreBucket+' ya existe en otra cuenta'
            case 'BucketAlreadyOwnedByYou':
                respuesta = 'El bucket '+nombreBucket+' ya existe en tu cuenta'
            case 'AccessDenied':
                respuesta = 'No se tienen permisos para crear el bucket'
            case _:
                respuesta = 'Error de cliente: '+e.response['Error']['Code']
    finally:
        return respuesta


if len(sys.argv)!= 3:
    print('Uso: create-bucket <nombre-bucket> <region>')
else:    
    response = crearBucketResource(sys.argv[1],sys.argv[2])
    # o bien
    # response = crearBucketClient(sys.argv[1],sys.argv[2])
    print(response)