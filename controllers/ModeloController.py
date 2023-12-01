from models.entitys import Modelo

class ModeloController():
    def __init__(self, session):
        self.session = session
    
    def create(self, modelo):
        try:
            #self.session.execute(text("INSERT INTO modelo (nome, idMarca) VALUES (:nome, :idMarca);", {"nome":modelo.nome, "idMarca":modelo.idMarca}))
            self.session.add(modelo)
            self.session.commit()
            return "Cadastrado com sucesso!"
        except Exception as e:
            self.session.rollback()
            return None
    
    def get(self, id):
        try:
            #SELECT * FROM modelo WHERE idModelo = :idModelo;
            return self.session.query(Modelo).filter(Modelo.idModelo == id).first()
        except Exception as e:
            return None
        
    def getAll(self):
        try:
            #SELECT * FROM modelo;
            return self.session.query(Modelo).all()
        except Exception as e:
            return None
        
    def update(self, modelo):
        try:
            #UPDATE modelo SET nome = :nome, idMarca = :idMarca WHERE idModelo = :idModelo;
            self.session.merge(modelo)
            self.session.commit()
            return "Atualizado com sucesso!"
        except Exception as e:
            self.session.rollback()
            return None
        
    def delete(self, modelo):
        try:
            #DELETE FROM modelo WHERE idModelo = :idModelo;
            self.session.delete(modelo)
            self.session.commit()
            return "Deletado com sucesso!"
        except Exception as e:
            self.session.rollback()
            return None