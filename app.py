from bottle import default_app
from config import Config


import controllers.livro_controller
import controllers.user_controller
import controllers.auth_controller
import controllers.emprestimo_controller 


class App:
    def __init__(self):
        self.bottle = default_app()
        self.config = Config()

    def setup_routes(self):
        from controllers import init_controllers
        print('🚀 Inicializa rotas!')
        init_controllers(self.bottle)

    def run(self):
        self.setup_routes()
        self.bottle.run(
            host=self.config.HOST,
            port=self.config.PORT,
            debug=self.config.DEBUG,
            reloader=self.config.RELOADER
        )

def create_app():
    return App()