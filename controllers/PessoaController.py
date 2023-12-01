from models.entitys import Pessoa
from sqlalchemy import text

class PessoaController:
    def __init__(self, session):
        self.session = session

    def create(self, pessoa):
        try:
            self.session.add(pessoa)
            self.session.commit()
            
            if pessoa.cpfConjuge != None:
                self.session.execute(text(f"call add_conjuge('{pessoa.cpf}', '{pessoa.cpfConjuge}');"))
            
            self.session.commit()
            
            return "Cadastrado com sucesso!"
        except Exception as e:
            self.session.rollback()
            return e
        
    def get(self, cpf):
        try:
            return self.session.query(Pessoa).filter(Pessoa.cpf == cpf).first()
        except Exception as e:
            return None
        
    def getAll(self):
        try:
            return self.session.query(Pessoa).all()
        except Exception as e:
            return e
    
    def update(self, pessoa):
        try:
            self.session.merge(pessoa)
            self.session.commit()
            return "Atualizado com sucesso!"
        except Exception as e:
            self.session.rollback()
            return None
        
    def delete(self, pessoa):
        try:
            self.session.delete(pessoa)
            self.session.commit()
            return "Deletado com sucesso!"
        except Exception as e:
            self.session.rollback()
            return e
    
