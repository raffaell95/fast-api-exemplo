from .rotas_produtos import *
from .rotas_auth import *
from .rotas_pedidos import *
from .TesteController import TesteController


class RouterController:

    def __init__(self, app) -> None:
        self.app = app
        
        
    def routers(self):
        return (
            self.app.include_router(rotas_produtos.router),
            self.app.include_router(rotas_auth.router),
            self.app.include_router(rotas_pedidos.router),
            self.app.include_router(TesteController.router())
        )
