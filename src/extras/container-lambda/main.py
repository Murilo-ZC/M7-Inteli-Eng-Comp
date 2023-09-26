import urllib.parse
import boto3

def handler(event, context):
    try:
        print("[TESTE-ELISA-MURILO]: Inicio da execução")
        s3 = boto3.client('s3')
        bucket = event['Records'][0]['s3']['bucket']['name']
        key_prefix = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
        print(f"[TESTE-ELISA-MURILO]: Bucket :{bucket} key_prefix: {key_prefix}")
        response = s3.get_object(Bucket=bucket, Key=key_prefix)
        s3.put_object(Bucket=f'{bucket}', Key=f'teste/{key_prefix}.okok', Body=response['Body'].read())
        print(f"[TESTE-ELISA-MURILO]: Fim da Execução")
        return {'message':'deu bom'}
    except Exception as e:
        print(f"[TESTE-ELISA-MURILO]: Algo deu errado - {str(e)}")
        return {'message':'deu ruim', 'error':str(e)}
