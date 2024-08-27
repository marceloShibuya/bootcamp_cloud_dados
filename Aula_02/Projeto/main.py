import os
from typing import List
import boto3
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações da AWS a partir do .env
AWS_ACCESS_KEY_ID: str = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY: str = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION: str = os.getenv('AWS_REGION')
BUCKET_NAME: str = os.getenv('BUCKET_NAME')

# Configura o cliente S3
s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
) 

# Joga os arquivos no S3
def listar_arquivos(pasta: str) -> List[str]:
    """Lista todos os arquivos em uma pasta local."""
    arquivos: List[str] = []
    for nome_arquivo in os.listdir(pasta):
        caminho_completo = os.path.join(pasta, nome_arquivo)
        if os.path.isfile(caminho_completo):
            arquivos.append(caminho_completo)
    return arquivos
