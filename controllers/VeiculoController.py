from models.entitys import Veiculo
from sqlalchemy import text

class VeiculoController:
    def __init__(self, session):
        self.session = session
        
    def create(self, veiculo):
        try:
            self.session.add(veiculo)
            self.session.commit()
            return "Cadastrado com sucesso!"
        except Exception as e:
            self.session.rollback()
            return None
    
    def maisVendidos(self):
        try:
            return self.session.execute(text("SELECT * FROM mais_vendidos")).fetchall()
        except Exception as e:
            return None
        
    def get(self, chassi):
        try:
            return self.session.query(Veiculo).filter_by(numeroChassi=chassi).first()
        except Exception as e:
            return None
        
    def getAll(self):
        try:
            return self.session.query(Veiculo).all()
        except Exception as e:
            return None
        
    def delete(self, veiculo):
        try:
            self.session.delete(veiculo)
            self.session.commit()
            return "Deletado com sucesso!"
        except Exception as e:
            self.session.rollback()
            return e
        
    def update(self, veiculo):
        try:
            self.session.merge(veiculo)
            self.session.commit()
            return "Atualizado com sucesso!"
        except Exception as e:
            self.session.rollback()
            return e