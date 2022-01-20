from jose import jwt
from datetime import datetime, timedelta
from src.infra.providers.env_provider import Env


def criar_access_token(data: dict):
    dados = data.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=int(Env('EXPIRES_IN_MIN').get()))
    dados.update({'exp': expiracao})
    
    token_jwt = jwt.encode(dados, Env('SECRET_KEY').get(), algorithm=Env('ALGORITHM').get())
    return token_jwt


def verificar_access_token(token: str):
    carga = jwt.decode(token, Env('SECRET_KEY').get(), algorithms=[Env('ALGORITHM').get()])
    return carga.get('sub')