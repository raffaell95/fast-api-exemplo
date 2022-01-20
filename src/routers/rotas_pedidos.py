from fastapi import Depends, status, APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.routers.auth_utils import obter_usuario_logado
from src.schemas import schemas
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.RepositorioPedido import RepositorioPedido


router = APIRouter()


@router.post('/pedidos', status_code=status.HTTP_201_CREATED, response_model=schemas.Pedido)
def fazer_pedido(pedido: schemas.Pedido, session: Session = Depends(get_db)):
    pedido_criado = RepositorioPedido(session).gravar_pedido(pedido)
    return pedido_criado

@router.get('/pedidos/{id}', response_model=schemas.Pedido)
def exibir_pedido(id: int, session: Session = Depends(get_db)):
    try:
        pedido = RepositorioPedido(session).buscar_por_id(id)
        return pedido
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Pedido não encontrado')

@router.get('/pedidos', response_model=List[schemas.Pedido])
def listar_pedido(usuario: schemas.Usuario = Depends(obter_usuario_logado), session: Session = Depends(get_db)):
    pedidos = RepositorioPedido(session).listar_meus_pedidos_por_usuario_id(usuario.id)
    return pedidos

@router.get('/pedidos/{usuario_id}/vendas', response_model=List[schemas.Pedido])
def listar_vendas(usuario_id: int, session: Session = Depends(get_db)):
    vandas = RepositorioPedido(session).listar_minhas_vendas_por_usuario_id(usuario_id)
    return vandas