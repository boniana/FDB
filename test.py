from controllers.Controller import Controller
from database.db import Session
from sqlalchemy import text



s = Session().createSession()

print(s.execute(text("""
    SELECT * FROM pessoa where cpf = '04126781013';
""")).fetchall())
s.commit()

con = Controller().pessoaController()
pessoa = con.get("04126781013")
print(pessoa.nome)