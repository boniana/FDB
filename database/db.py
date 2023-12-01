from sqlalchemy import create_engine, text, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from dotenv import load_dotenv
import os
from models.entitys import Base

load_dotenv()

config = {
    "user":os.getenv('USER'),
    "password":os.getenv('PASSWORD'),
    "host":"localhost",
    "port":"3306",
    "database":os.getenv('DATABASE')
}

class Session:
    def __init__(self):
        self.createNewDados = False
        self.createSession()
        self.createDatabase()
        
    def createSession(self):
        try:
            self.engine = create_engine(f"mysql+pymysql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}")
            if not database_exists(self.engine.url):
                create_database(self.engine.url)
                self.createNewDados = True
                
        except Exception as e:
            print(e)
            return None

        session = sessionmaker(bind=self.engine)()
        
        return session

    def createDatabase(self):
        Base.metadata.create_all(self.engine)
        self.add_trigger_insert_venda()
        self.add_trigger_update_venda()
        self.add_trigger_after_insert_pessoa()
        self.add_procedure_conjuge()
        self.createViewMaisVendidos()
        
     
    def createViewMaisVendidos(self):
        try:
            self.engine.connect().execute(text("DROP VIEW IF EXISTS mais_vendidos;"))
            self.engine.connect().execute(text("""
                CREATE VIEW mais_vendidos AS
                SELECT modelo.nome as modelo, marca.nome as marca, count(*) AS quantidade from venda NATURAL JOIN veiculo
                JOIN modelo ON veiculo.idModelo = modelo.idModelo JOIN marca ON
                    marca.idMarca = modelo.idMarca GROUP BY modelo.idModelo order by quantidade desc
                ;
            """))
            self.engine.connect().commit()
        except Exception as e:
            print(e)   
            
    def add_procedure_conjuge(self):
        procedure_sql = text("""
            CREATE PROCEDURE add_conjuge(IN cpfN VARCHAR(11), IN cC VARCHAR(11))
            BEGIN
                IF cC IS NOT NULL THEN
                    UPDATE pessoa
                    SET cpfConjuge = cpfN, estadoCivil = 'Casado'
                    WHERE cpf = cC;
                END IF;
            END;
        """)
        
        self.engine.connect().execute(text("DROP PROCEDURE IF EXISTS add_conjuge;"))
        self.engine.connect().execute(procedure_sql)
        self.engine.connect().execute(text("GRANT EXECUTE ON PROCEDURE trabalhofbd.add_conjuge TO 'root'@'localhost';"))
        self.engine.connect().commit()         
    
    def add_trigger_after_insert_pessoa(self):
        trigger_sql = text("""
            CREATE TRIGGER after_insert_pessoa
            BEFORE INSERT ON pessoa
            FOR EACH ROW
            BEGIN
                IF NEW.estadoCivil <> 'Casado' THEN
                    SET NEW.cpfConjuge = NULL;
                END IF;
            END;
        """)
        
        self.engine.connect().execute(text("DROP TRIGGER IF EXISTS after_insert_pessoa;"))
        self.engine.connect().execute(trigger_sql)
        self.engine.connect().commit()
    
    
    def add_trigger_update_venda(self):
        trigger_sql = text("""
            CREATE TRIGGER before_update_venda
            BEFORE UPDATE ON venda
            FOR EACH ROW
            BEGIN
                DECLARE chassi_veiculo VARCHAR(255);
                DECLARE cpf_comprador VARCHAR(255);
                DECLARE data_venda DATE;
                DECLARE data_existe DATE;

                SELECT NEW.numeroChassi, NEW.cpfCompra, NEW.data INTO chassi_veiculo, cpf_comprador, data_venda;
                SELECT MAX(data) INTO data_existe FROM venda WHERE numeroChassi = chassi_veiculo;
                
                IF data_existe IS NULL OR data_venda > data_existe THEN
                    UPDATE veiculo
                    SET cpfProprietario = cpf_comprador
                    WHERE numeroChassi = chassi_veiculo;
                END IF;
                
            END;
        """)
        
        self.engine.connect().execute(text("DROP TRIGGER IF EXISTS before_update_venda;"))
        self.engine.connect().execute(trigger_sql)
        self.engine.connect().commit()
        
    def add_trigger_insert_venda(self):
        trigger_sql = text("""
            CREATE TRIGGER before_insert_venda
            BEFORE INSERT ON venda
            FOR EACH ROW
            BEGIN
                DECLARE chassi_veiculo VARCHAR(255);
                DECLARE cpf_comprador VARCHAR(255);
                DECLARE data_venda DATE;
                DECLARE data_existe DATE;

                SELECT NEW.numeroChassi, NEW.cpfCompra, NEW.data INTO chassi_veiculo, cpf_comprador, data_venda;
                SELECT MAX(data) INTO data_existe FROM venda WHERE numeroChassi = chassi_veiculo;
                
                IF data_existe IS NULL OR data_venda > data_existe THEN
                    UPDATE veiculo
                    SET cpfProprietario = cpf_comprador
                    WHERE numeroChassi = chassi_veiculo;
                END IF;
                
            END;
        """)

        self.engine.connect().execute(text("DROP TRIGGER IF EXISTS before_insert_venda;"))
        self.engine.connect().execute(trigger_sql)
        self.engine.connect().commit()




