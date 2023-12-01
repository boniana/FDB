from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, String, Integer, ForeignKey, Date, Float
from sqlalchemy.orm import relationship, backref

class Base(DeclarativeBase):
    pass

class Pessoa(Base):
    __tablename__ = 'pessoa'
    cpf = Column(String(11), primary_key=True)
    nome = Column(String(100), nullable=False)
    estadoCivil = Column(String(20))
    endereco = Column(String(100), nullable=False)
    cpfConjuge = Column(String(11), ForeignKey('pessoa.cpf'))
    conjuge = relationship('Pessoa', foreign_keys=[cpfConjuge])
    mysql_engine = 'myisam'

    def __repr__(self):
        return f'Pessoa(cpf={self.cpf}, nome={self.nome}, estadoCivil={self.estadoCivil}, endereco={self.endereco}, cpfConjuge={self.cpfConjuge})'

    
class Telefone(Base):
    __tablename__ = 'telefone'
    cpf = Column(String(11), ForeignKey('pessoa.cpf'), primary_key=True)
    pessoa = relationship('Pessoa', foreign_keys=[cpf], backref=backref('telefones', cascade='all, delete-orphan'))
    telefone = Column(String(11), primary_key=True)
    ddd = Column(String(2), nullable=False)

    def __repr__(self):
        return f'Telefone(cpf={self.cpf}, telefone={self.telefone}, ddd={self.ddd})'
    
class Marca(Base):
    __tablename__ = 'marca'
    idMarca = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)

    def __repr__(self):
        return f'Marca(nome={self.nome})'
    
class Modelo(Base):
    __tablename__ = 'modelo'
    idModelo = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    idMarca = Column(Integer, ForeignKey('marca.idMarca'))
    marca = relationship('Marca', foreign_keys=[idMarca], backref=backref('modelos', cascade='all, delete-orphan'))

    def __repr__(self):
        return f'Modelo(nome={self.nome}, idMarca={self.idMarca})'
    
class Veiculo(Base):
    __tablename__ = 'veiculo'
    numeroChassi = Column(String(17), primary_key=True)
    idModelo = Column(Integer, ForeignKey('modelo.idModelo'))
    modelo = relationship('Modelo', foreign_keys=[idModelo], backref=backref('veiculos', cascade='all, delete-orphan'))
    cor = Column(String(20), nullable=False)
    ano = Column(Integer, nullable=False)
    cpfProprietario = Column(String(11), ForeignKey('pessoa.cpf'), nullable=False)
    proprietario = relationship('Pessoa', foreign_keys=[cpfProprietario], backref=backref('veiculos', cascade='all, delete-orphan'))

    def __repr__(self):
        return f'Veiculo(numeroChassi={self.numeroChassi}, idModelo={self.idModelo}, cor={self.cor}, ano={self.ano})'

class Venda(Base):
    __tablename__ = 'venda'
    idVenda = Column(Integer, primary_key=True, autoincrement=True)
    numeroChassi = Column(String(17), ForeignKey('veiculo.numeroChassi'))
    veiculo = relationship('Veiculo', foreign_keys=[numeroChassi], backref=backref('vendas', cascade='all, delete-orphan'))
    cpfVendedor = Column(String(11), ForeignKey('pessoa.cpf'))
    vendedor = relationship('Pessoa', foreign_keys=[cpfVendedor])
    cpfCompra = Column(String(11), ForeignKey('pessoa.cpf'))
    comprador = relationship('Pessoa', foreign_keys=[cpfCompra])
    preco = Column(Float, nullable=False)
    data = Column(Date, nullable=False)

    def __repr__(self):
        return f'Venda(idVenda={self.idVenda}, cpfVendedor={self.cpfVendedor}, cpfCompra={self.cpfCompra}, preco={self.preco}, data={self.data})'

