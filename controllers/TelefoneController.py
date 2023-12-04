from models.entitys import Telefone

class TelefoneController:
    
    def __init__(self, session):
        self.session = session

    def create(self, telefone):
        try:
            ##insert into telefone (cpf, telefone) values (:cpf, :telefone);
            self.session.add(telefone)
            self.session.commit()
            return "Cadastrado com sucesso!"
        except Exception as e:
            self.session.rollback()
            return e
        
    def getAll(self, cpf):
        ##select * from telefone where cpf = :cpf;
        return self.session.query(Telefone).filter(Telefone.cpf == cpf).all()
    
    def update(self, telefone):
        try:
        ##update telefone set telefone = :telefone where cpf = :cpf and telefone = :telefone;
            self.session.merge(telefone)
            self.session.commit()
            return "Atualizado com sucesso!"
        except Exception as e:
            self.session.rollback()
            return e
    
    def delete(self, cpf, telefone):
        ##delete from telefone where cpf = :cpf and telefone = :telefone;
        try:
            t = self.get(cpf, telefone)
            self.session.delete(t)
            self.session.commit()
            return "Deletado com sucesso!"
        except Exception as e:
            self.session.rollback()
            return e