from models.entitys import Marca
from sqlalchemy import text

class MarcaController:
    def __init__(self, session):
        self.session = session
        
    def create(self, marca):
        try:
            #self.session.execute(text("""
            #    Insert into marca (nome) values (:nome);
            #                          """, {"nome":marca.nome}))
            self.session.add(marca)
            self.session.commit()
            return "Cadastrado com sucesso!"
        except Exception as e:
            self.session.rollback()
            return e
        
    def getIdByNome(self, nome):
        try:
            #SELECT idMarca FROM marca WHERE nome = :nome;
            return self.session.query(Marca).filter(Marca.nome == nome).first().idMarca
        except Exception as e:
            return e    
    
    def getAll(self):
        #SELECT * FROM marca;
        marcas = self.session.query(Marca).all()
        return marcas
    
    def get(self, idMarca):
        #SELECT * FROM marca WHERE idMarca = :idMarca;
        marca = self.session.query(Marca).filter(Marca.idMarca == idMarca).first()
        return marca
    
    def update(self, marca):
        try:
            #UPDATE marca SET nome = :nome WHERE idMarca = :idMarca;
            self.session.merge(marca)
            self.session.commit()
            return "Atualizado com sucesso!"
        except Exception as e:
            self.session.rollback()
            return e
        
    def delete(self, marca):
        try:
            #DELETE FROM marca WHERE idMarca = :idMarca;
            self.session.delete(marca)
            self.session.commit()
            return "Deletado com sucesso!"
        except Exception as e:
            self.session.rollback()
            return e