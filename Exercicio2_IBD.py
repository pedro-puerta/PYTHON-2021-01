import sqlalchemy

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

# Criar Conexão com Banco SQLITE
# caso o arquivo não exista, ele será criado
engine = sqlalchemy.create_engine("sqlite:///serverEx2.db")
connection = engine.connect()

# Criar sessão com o Banco de Dados
Base = declarative_base(engine)
session = Session()


# Criar tabela no banco de dados, caso não exista
connection.execute("""CREATE TABLE IF NOT EXISTS FUNCIONARIO (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255) NOT NULL,
                        IDADE INT NOT NULL,
                        SALARIO FLOAT NOT NULL)
                    """)


# Mapeamento da tabela
class Funcionario(Base):
    __tablename__ = 'FUNCIONARIO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))
    idade = Column('IDADE', Integer)
    salario = Column('SALARIO', Float)

    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario


lista_func = []
base_func = open('funcionarios.txt', 'r')

for linha in base_func:
    linha = linha.split(';')
    funcionario = Funcionario(linha[0], int(linha[1]), float(linha[2]))
    lista_func.append(funcionario)

session.add_all(lista_func)

result = session.query(Funcionario).all()
for i in result:
    print('Número de inscrição:', i.id, '| Nome:', i.nome,
          '| Idade:', i.idade, '| Salário:', i.salario)
    print('-'*80)

session.commit()

session.close()
