
from fastapi import Depends, status, APIRouter, HTTPException
from src.infra.sqlalchemy.repositorios.RepositorioProduto import RepositorioProduto
from sqlalchemy.orm import Session
from typing import List
from src.schemas import schemas
from src.infra.sqlalchemy.config.database import get_db
from src.routers.auth_utils import obter_usuario_logado



router = APIRouter()


@router.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=schemas.Produto)
def criar_produtos(produto: schemas.Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado

@router.get('/produtos', status_code=status.HTTP_200_OK, response_model=List[schemas.ProdutoSimples])
def listar_rodutos(db: Session = Depends(get_db), usuario: schemas.Usuario = Depends(obter_usuario_logado)):
    produtos = RepositorioProduto(db).listar()
    return produtos

@router.get('/produtos/{id}', status_code=status.HTTP_200_OK, response_model=schemas.Produto)
def exibir_produto(id: int, session: Session = Depends(get_db)):
    produto_localizado = RepositorioProduto(session).buscarPorId(id)
    if not produto_localizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não há um produto com esse id {id}')
    return produto_localizado

@router.put('/produtos/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ProdutoSimples)
def atualizar_produto(id: int, produto: schemas.Produto, session: Session = Depends(get_db)):
    RepositorioProduto(session).editar(id, produto)
    produto.id = id
    return produto

@router.delete('/produtos/{id}')
def remover_produto(id: int, session: Session = Depends(get_db)):
    RepositorioProduto(session).remover(id)
    return