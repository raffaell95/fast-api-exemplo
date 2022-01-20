from src.routers.base_controller import BaseController

controller = BaseController.prefix('/controller')

@controller.resource()
class TesteController:

    @controller.route.get('/')
    def novo_teste(self):
        return {'MSG': 'Testando controller'}