from controllers.PessoaController import PessoaController
from controllers.TelefoneController import TelefoneController
from controllers.MarcaController import MarcaController
from controllers.ModeloController import ModeloController
from controllers.VeiculoController import VeiculoController
from controllers.VendaController import VendaController
from database.db import Session


class Controller:
    def __init__(self):
        self.session = Session().createSession()

    def pessoaController(self):
        return PessoaController(self.session)
    
    def telefoneController(self):
        return TelefoneController(self.session)
    
    def marcaController(self):
        return MarcaController(self.session)
    
    def modeloController(self):
        return ModeloController(self.session)
    
    def veiculoController(self):
        return VeiculoController(self.session)
    
    def vendaController(self):
        return VendaController(self.session)