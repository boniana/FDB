from database.db import Session
from sqlalchemy import text
from models.entitys import Marca

s = Session().createSession()
t = s.execute(text("Select * from marca where nome = :nome ;").bindparams(nome="Honda")).first()

print(t)