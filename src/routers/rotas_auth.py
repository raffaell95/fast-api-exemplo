from fastapi import APIRouter, HTTPException
from src.infra.sqlalchemy.repositorios.RepositorioUsuario import RepositorioUsuario
from src.infra.sqlalchemy.config.database import get_db
from src.schemas import schemas
from fastapi import Depends, status
from sqlalchemy.orm import Session
from typing import List
from src.infra.providers import hash_provider, token_provider
from src.routers.auth_utils import obter_usuario_logado


router = APIRouter(prefix='/auth')


@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=schemas.UsuarioSimples)
def signup(usuario: schemas.Usuario, session: Session = Depends(get_db)):

    usuario_localizado = RepositorioUsuario(session).obter_por_telefone(usuario.telefone)
    if usuario_localizado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Já existe um usuario para esse telefone')

    usuario.senha = hash_provider.gerar_hash(usuario.senha)
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado


@router.post('/token', response_model=schemas.LoginSucesso)
def login(login_data: schemas.LoginData, session: Session = Depends(get_db)):
    senha = login_data.senha
    telefone =  login_data.telefone

    usuario = RepositorioUsuario(session).obter_por_telefone(telefone)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Usuario não corresponde')
    
    senha_valida = hash_provider.verificar_hash(senha, usuario.senha)
    if not senha_valida:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='A Senha não corresponde')
    
    token = token_provider.criar_access_token({'sub': usuario.telefone})
    return schemas.LoginSucesso(usuario=usuario, access_token=token)


@router.get('/me', response_model=schemas.UsuarioSimples)
def me(usuario: schemas.Usuario = Depends(obter_usuario_logado)):
    return usuario
