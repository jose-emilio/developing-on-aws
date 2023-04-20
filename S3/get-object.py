import boto3
from botocore.exceptions import ClientError
import sys

# Uso de la llamada a la API GetObject
# Obtiene un objeto indicado por una clave en un bucket de S3
def obtenerObjeto(nombreBucket,clave,fichero):
    session = boto3.Session(profile_name='lab')
    try:
        client = session.client('s3')
        with open(fichero,'wb') as f:        
            client.download_fileobj(nombreBucket,clave,f)
        respuesta = 'Objeto obtenido satisfactoriamente'
    except ClientError as e:
        match e.response['Error']['Code']:
            case '404':
                respuesta = 'El objeto no existe en el bucket'
            case '403':
                respuesta = 'No se tienen permisos para acceder al objeto'
            case _:
                respuesta = 'Error de cliente: '+e.response['Error']['Message']
    finally:
        return respuesta

if len(sys.argv)!= 4:
    print('Uso: get-object <nombre-bucket> <clave-objeto> <nombre-fichero>')
else:    
    respuesta = obtenerObjeto(sys.argv[1],sys.argv[2],sys.argv[3])
    print(respuesta)