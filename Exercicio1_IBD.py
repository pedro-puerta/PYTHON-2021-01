import sqlalchemy

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

# Criar Conexão com Banco SQLITE
# caso o arquivo não exista, ele será criado
engine = sqlalchemy.create_engine("sqlite:///serverEx1.db")
connection = engine.connect()

# Criar sessão com o Banco de Dados
Base = declarative_base(engine)
session = Session()


# Criar tabela PACIENTE, caso não exista
connection.execute("""CREATE TABLE IF NOT EXISTS PACIENTE (
                        ID    INTEGER      PRIMARY KEY,
                        NOME  VARCHAR(255) NOT NULL,
                        CPF   VARCHAR(20)  NOT NULL,
                        IDADE INT          NOT NULL)
                    """)


# Criar tabela MEDICO, caso não exista
connection.execute("""CREATE TABLE IF NOT EXISTS MEDICO (
                        ID             INTEGER      PRIMARY KEY,
                        NOME           VARCHAR(255) NOT NULL,
                        CRM            VARCHAR(20)  NOT NULL,
                        ESPECIALIZACAO VARCHAR(255) NOT NULL)
                    """)


# Criar tabela EXAME, caso não exista
connection.execute("""CREATE TABLE IF NOT EXISTS EXAME (
                        ID          INTEGER      PRIMARY KEY,
                        ID_MEDICO   INT          NOT NULL,
                        ID_PACIENTE INT          NOT NULL,
                        DESCRICAO   VARCHAR(500) NOT NULL,
                        RESULTADO   VARCHAR(500) NOT NULL)
                    """)


# Mapeamento das tabelas
class Paciente(Base):
    __tablename__ = 'PACIENTE'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))
    cpf = Column('CPF', String(20))
    idade = Column('IDADE', Integer)

    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade


class Medico(Base):
    __tablename__ = 'Medico'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))
    crm = Column('CRM', String(20))
    especializacao = Column('ESPECIALIZACAO', String(255))

    def __init__(self, nome, crm, especializacao):
        self.nome = nome
        self.crm = crm
        self.especializacao = especializacao


class Exame(Base):
    __tablename__ = 'EXAME'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    id_medico = Column('ID_MEDICO', Integer)
    id_paciente = Column('ID_PACIENTE', Integer)
    descricao = Column('DESCRICAO', String(255))
    resultado = Column('RESULTADO', String(255))

    def __init__(self, id_medico, id_paciente, descricao, resultado):
        self.id_medico = id_medico
        self.id_paciente = id_paciente
        self.descricao = descricao
        self.resultado = resultado


# Criando Objetos
paciente1 = Paciente('Pedro', '12345678-x', 22)
paciente2 = Paciente('Emma', '43215678-x', 23)
medico = Medico('Guilherme', '24111995', 'Clínico Geral')
exame1 = Exame(1, 1, 'Paciente está com dor de cabeça', 'Deve tomar dipirona')
exame2 = Exame(1, 2, 'Paciente está com virose', 'Deve tomar besetacil')

# Adicionando no Banco de Dados
session.add(paciente1)
session.add(paciente2)
session.add(medico)
session.add(exame1)
session.add(exame2)

# Confirmando
session.commit()

# Buscando os dados da tabela Paciente
print('-'*30)
resultPaciente = session.query(Paciente).all()
for i in resultPaciente:
    print(i.id, i.nome, i.cpf, i.idade)

# Buscando os dados da tabela Paciente
print('-'*30)
resultMedico = session.query(Medico).all()
for i in resultMedico:
    print(i.id, i.nome, i.crm, i.especializacao)

# Buscando os dados da tabela Paciente
print('-'*30)
resultExames = session.query(Exame).all()
for i in resultExames:
    print(i.id, i.id_medico, i.id_paciente, i.descricao, i.resultado)

# Fechando a conexão
connection.close()
