from fastapi_router_controller import Controller
from fastapi import APIRouter


class BaseController:

    def prefix(pre: str) -> Controller:
        return Controller(APIRouter(prefix=pre))