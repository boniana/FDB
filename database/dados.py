from controllers.Controller import Controller
from models.entitys import Pessoa, Venda, Veiculo, Modelo, Marca, Telefone
from faker import Faker

def create_dados():
    print("Criando dados...")
    controller = Controller()
    conPessoa = controller.pessoaController()

    fake = Faker('pt_BR')
    for i in range(100):
        nome = fake.name()
        cpf = fake.cpf().replace('.', '').replace('-', '')
        endereco = fake.address()
        estadoCivil = fake.random_element(elements=('Solteiro', 'Casado', 'Divorciado', 'Viúvo'))
        cpfConjuge = None
        if estadoCivil == 'Casado':
            pessoas = conPessoa.getAll()
            if pessoas:
                cpfConjuge = fake.random_element(elements=pessoas).cpf
            
        pessoa = Pessoa(
            nome = nome,
            cpf = cpf,
            endereco = endereco,
            estadoCivil = estadoCivil,
            cpfConjuge = cpfConjuge
        )
        
        try:
            p = conPessoa.create(pessoa)
            if p != "Cadastrado com sucesso!":
                raise Exception(p)
        except Exception as e:
            print(e)

    pessoas = conPessoa.getAll()
    conTelefone = controller.telefoneController()
    for i in range(100):
        try:
            telefone = fake.msisdn()[2:]
            ddd = fake.random_int(min=11, max=99)
            cpf = fake.random_element(elements=pessoas).cpf
            t = Telefone(telefone= telefone, ddd = ddd, cpf = cpf)
            conTelefone.create(t)
        except Exception as e:
            print(e)
    
    
    conMarca = controller.marcaController()
    for i in ["BMW", "Mercedes", "Audi", "Volkswagen", "Chevrolet", "Renault", "Hyundai", "Toyota", "Honda", "Nissan"]:
        marca = Marca(nome=i)
        try:
            conMarca.create(marca)
        except Exception as e:
            print(e)
           
    modelos = {
        "BMW": ["Série 1", "Série 2", "Série 3", "Série 4", "Série 5", "Série 6", "Série 7", "Série 8", "X1", "X2", "X3", "X4", "X5", "X6", "X7", "Z4"],
        "Mercedes": ["Classe A", "Classe B", "Classe C", "Classe E", "Classe S", "Classe G", "Classe GL", "Classe GLA", "Classe GLB", "Classe GLC", "Classe GLE", "Classe GLS", "Classe SLC", "Classe SL", "Classe SLK"],
        "Audi": ["A1", "A3", "A4", "A5", "A6", "A7", "A8", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "TT"],
        "Volkswagen": ["Gol", "Fox", "Polo", "Voyage", "Virtus", "Golf", "Jetta", "Passat", "Tiguan", "T-Cross", "Amarok", "Saveiro", "Up", "Nivus", "Tiguan Allspace"],
        "Chevrolet": ["Onix", "Onix Plus", "Prisma", "Cruze", "Cobalt", "Spin", "Tracker", "Trailblazer", "S10", "Equinox", "Camaro", "Bolt"],
        "Renault": ["Kwid", "Sandero", "Logan", "Duster", "Captur", "Stepway", "Duster Oroch", "Kangoo", "Master", "Alaskan", "Zoe"],
        "Hyundai": ["HB20", "HB20S", "HB20X", "Creta", "i30", "iX35", "Azera", "Santa Fe", "Tucson", "Elantra", "Veloster", "HR", "i30 CW", "i30 N"],
        "Toyota": ["Etios", "Corolla", "Prius", "Camry", "Hilux", "SW4", "RAV4", "Yaris", "Yaris Sedan", "Land Cruiser", "Supra"],
        "Honda": ["Fit", "City", "Civic", "HR-V", "WR-V", "CR-V", "Civic Si", "Accord", "Civic Type R"],
        "Nissan": ["March", "Versa", "Kicks", "Sentra", "GT-R", "Frontier", "Leaf", "X-Trail", "Altima"]
    }
    
    conModelo = controller.modeloController()
    for marca in modelos:
        for modelo in modelos[marca]:
            try:
                m = Modelo(nome=modelo, idMarca=conMarca.getIdByNome(marca))
                conModelo.create(m)
                
            except Exception as e:
                print(e)
 
    conVeiculo = controller.veiculoController()      
    modelos_v = conModelo.getAll()  
    for i in range(100):
        try:
            numeroChassi = str(fake.ean(length=13)) + str(fake.ean(length=8)[:4])
            
            veiculo = Veiculo(
                numeroChassi=numeroChassi,
                idModelo=fake.random_element(modelos_v).idModelo,
                cor = fake.color_name(),
                ano = fake.random_int(min=1990, max=2020),
                cpfProprietario = fake.random_element(pessoas).cpf
            )
            conVeiculo.create(veiculo)
        except Exception as e:
            print(e)