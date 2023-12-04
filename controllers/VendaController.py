from models.entitys import Venda

class VendaController:
    def __init__(self, session):
        self.session = session
        
    def create(self, venda):
        try:
            self.session.add(venda)
            self.session.commit()
            return "Cadastrado com sucesso!"
        except Exception as e:
            self.session.rollback()
            return e
        
    def get(self, id):
        try:
            return self.session.query(Venda).filter_by(idVenda=id).first()
        except Exception as e:
            return None
        
    def getAll(self):
        try:
            return self.session.query(Venda).all()
        except Exception as e:
            return None
        
    def delete(self, venda):
        try:
            self.session.delete(venda)
            self.session.commit()
            return "Deletado com sucesso!"
        except Exception as e:
            self.session.rollback()
            return e
    
    def update(self, venda):
        try:
            self.session.merge(venda)
            self.session.commit()
            return "Atualizado com sucesso!"
        except Exception as e:
            self.session.rollback()
            return None