import boto3
from botocore.exceptions import ClientError
import sys

# Carga multiparte mediante la API de bajo nivel de S3
def crearCargaMultiparte(client,resource,bucket,fichero):
    
    cargaMultiparte = client.create_multipart_upload(
        Bucket=bucket,
        ContentType='application/vnd.openxmlformats-officedocument.presentationml.presentation',
        Key=fichero
    )

    with open(fichero,'rb') as f:
        nParte = 1
        partes = []
        #El tamaño mínimo de cada parte debe ser al meno 5 MB, excepto la última, sino lanza una excepción EntityTooSmall
        tamano = 5 * 1024 * 1024
        while True:
            fragmento = f.read(tamano)
            if fragmento == b'':
                break
            cargaParte = resource.MultipartUploadPart(bucket,fichero,cargaMultiparte['UploadId'],nParte)
            print('Cargando parte '+str(nParte)+'...')
            respuestaCargaParte = cargaParte.upload(Body=fragmento)
            print('Parte '+str(nParte)+' cargada con éxito !!')
            partes.append(
                {
                    'PartNumber': nParte,
                    'ETag': respuestaCargaParte['ETag']
                }
            )
            nParte = nParte + 1
        resultado = client.complete_multipart_upload(
            Bucket=bucket,
            Key=fichero,
            MultipartUpload={
                'Parts': partes
            },
            UploadId=cargaMultiparte['UploadId']
        )


if len(sys.argv)!= 3:
    print('Uso: multi-part-upload <nombre-bucket> <fichero-PPTX>')
else:
    session = boto3.Session(profile_name='lab')
    s3client = session.client('s3')
    s3resource = session.resource('s3')    
    crearCargaMultiparte(s3client,s3resource,sys.argv[1],sys.argv[2])