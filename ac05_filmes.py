# ATIVIDADE CONTÍNUA 05

# NOMES DOS ALUNOS: (MÁXIMO 6):
# ALUNO 1: Pedro Silverio Puerta
# ALUNO 2: Adalto de Almeida Linhares Santos
# ALUNO 3: nome
# ALUNO 4: nome
# ALUNO 5: nome
# ALUNO 6: nome


import sqlalchemy

from sqlalchemy import Column, Integer, String, Float, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.sql.sqltypes import FLOAT

# Criar Conexão com Banco SQLITE
engine = sqlalchemy.create_engine("sqlite:///server.db")
connection = engine.connect()
Base = declarative_base(engine)
session = Session()


class Filme(Base):

    # FAZER O MAPEAMENTO DA TABELA
    __tablename__ = 'FILME'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    titulo = Column('TITULO', String(255), nullable=False)
    ano = Column('ANO', Integer, nullable=False)
    genero = Column('GENERO', String(255), nullable=False)
    duracao = Column('DURACAO', Integer, nullable=False)
    pais = Column('PAIS', String(255), nullable=False)
    diretor = Column('DIRETOR', String(255), nullable=False)
    elenco = Column('ELENCO', String(255), nullable=False)
    avaliacao = Column('AVALIACAO', Float, nullable=False)
    votos = Column('VOTOS', Integer, nullable=False)

    # Método construtor
    def __init__(self, titulo, ano, genero, duracao, pais, diretor, elenco,
                 avaliacao, votos):
        self.titulo = titulo
        self.ano = ano
        self.genero = genero
        self.duracao = duracao
        self.pais = pais
        self.diretor = diretor
        self.elenco = elenco
        self.avaliacao = avaliacao
        self.votos = votos


# Classe para interação com o Banco de Dados
class BancoDeDados:
    def criar_tabela(self):
        # Cria a tabela FILME no banco de dados
        connection.execute("""CREATE TABLE IF NOT EXISTS FILME(
                              ID INTEGER PRIMARY KEY,
                              TITULO VARCHAR(255) NOT NULL,
                              ANO INT NOT NULL,
                              GENERO VARCHAR(255) NOT NULL,
                              DURACAO INT NOT NULL,
                              PAIS VARCHAR(255) NOT NULL,
                              DIRETOR VARCHAR(255) NOT NULL,
                              ELENCO VARCHAR(255) NOT NULL,
                              AVALIACAO FLOAT NOT NULL,
                              VOTOS INT NOT NULL)""")

    def incluir(self, filme):
        '''
        Recebe um objeto Filme e armazena esse
        objeto no banco de dados.
        '''
        session.add(filme)
        session.commit()

    def incluir_lista(self, filmes):
        '''
        Recebe uma lista de objetos Filme e armazena esses
        objetos no banco de dados
        '''
        session.add_all(filmes)
        session.commit()

    def alterar_avaliacao(self, filme, avaliacao):
        '''
        Recebe um objeto filme e altera sua avaliação de
        acordo com o valor do parametro avaliacao
        '''
        # Alterar um registro
        filme = session.query(Filme).get(filme.id)
        # altera os atributos do objeto
        filme.avaliacao = avaliacao
        session.commit()

    def excluir(self, id):
        '''
        Recebe o id de um filme e exclui o filme correspondente
        do banco de dados
        '''
        filme = session.query(Filme).get(id)
        if filme is not None:
            session.delete(filme)
            session.commit()

    def buscar_todos(self):
        '''
        Realiza busca no banco de dados e retorna uma
        lista de objetos Filme com todos os registros,
        ordenados de forma crescente pelo titulo.
        '''
        filmes = session.query(Filme).order_by(Filme.titulo).all()
        return filmes

    def buscar_por_id(self, id):
        '''
        Realiza busca no banco de dados e retorna um
        objeto Filme de acordo com o seu id
        '''
        filme = session.query(Filme).get(id)
        return filme

    def buscar_por_ano(self, ano):
        '''
        Realiza busca no banco de dados e retorna uma
        lista de objetos Filme de um ano específico,
        ordenado pelo ID de forma crescente
        '''
        filmes = session.query(Filme).filter(
            Filme.ano == ano).order_by(Filme.id).all()
        return filmes

    def buscar_por_genero(self, genero):
        '''
        Realiza busca no banco de dados e retorna uma
        lista de objetos Filme de um gênero específico,
        ordenados pelo titulo de forma crescente
        '''
        filmes = session.query(Filme).filter(Filme.genero.like(
            '%' + genero + '%')).order_by(Filme.titulo).all()
        return filmes

    def buscar_por_elenco(self, ator):
        '''
        Realiza busca no banco de dados e retorna uma
        lista de objetos Filme que tenha um determinado ator/atriz como parte
        do elenco, ordenados pelo ano de lançamento em ordem crescente
        '''
        filmes = session.query(Filme).filter(Filme.elenco.like(
            '%' + ator + '%')).order_by(Filme.ano).all()
        return filmes

    def buscar_melhores_do_ano(self, ano):
        '''
        Realiza busca no banco de dados e retorna uma lista de
        objetos Filme de um ano específico, com avaliação
        maior ou igual a 90
        Deve retornar ordenado pela avaliação de forma decrescente.
        DICA - utilize a função:
            .order_by(desc(Filme.avaliacao))
        '''
        filmes = []
        todos_filmes = session.query(Filme).filter(
            Filme.ano == ano).order_by(desc(Filme.avaliacao)).all()
        for i in todos_filmes:
            if i.avaliacao >= 90.0:
                filmes.append(i)
        return filmes

    def exportar_filmes(self, nome_arquivo):
        '''
        Exporta os dados contidos na tabela de filmes para um arquivo de texto
        O arquivo deve conter uma listagem dos filmes, ordenados pelos titulos
        dos filmes, contendo os dados de cada filme em uma linha, no formato:
        titulo;ano;genero;duracao;país;diretor;elenco;avaliacao;votos
        '''
        export = open(nome_arquivo, 'w', encoding="utf-8")
        filmes = session.query(Filme).order_by(Filme.titulo).all()
        for i in filmes:
            escreva = i.titulo + ';' + str(i.ano) + ';' \
                + i.genero + ';' + str(i.duracao) + ';' \
                + i.pais + ';' + i.diretor + ';' \
                + i.elenco + ';' + str(i.avaliacao) + ';' \
                + str(i.votos)
            export.write(escreva)
        export.close()

    def importar_filmes(self, nome_arquivo):
        '''
        Recebe como parâmetro o nome de um arquivo de texto e importa os
        dados contidos no arquivo para o banco de dados.
        Considere que o arquivo contém uma listagem de filmes no formato:
        titulo;year;genero;duracao;país;diretor;elenco;avaliacao;votos
        '''
        lista_filmes = []
        base_filmes = open(nome_arquivo, 'r', encoding="utf-8")
        for linha in base_filmes:
            linha = linha.split(';')
            titulo = linha[0]
            ano = int(linha[1])
            genero = linha[2]
            duracao = int(linha[3])
            pais = linha[4]
            diretor = linha[5]
            elenco = linha[6]
            avaliacao = float(linha[7])
            votos = int(linha[8])
            filme = Filme(titulo, ano, genero, duracao, pais,
                          diretor, elenco, avaliacao, votos)
            lista_filmes.append(filme)
        base_filmes.close()
        session.add_all(lista_filmes)
        session.commit()


# EXEMPLO DE PROGRAMA PRINCIPAL
banco = BancoDeDados()
banco.criar_tabela()
banco.importar_filmes('movies.txt')

# Busca todos os filmes
lista = banco.buscar_todos()
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.genero, f.duracao,
          f.pais, f.diretor, f.elenco, f.avaliacao, f.votos)

# Busca por ano
lista = banco.buscar_por_ano(2019)
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.genero, f.duracao,
          f.pais, f.diretor, f.elenco, f.avaliacao, f.votos)

# Busca por genero
lista = banco.buscar_por_genero('Crime')
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.genero)

# Busca por elenco
lista = banco.buscar_por_elenco('Nicole')
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.genero, f.duracao,
          f.pais, f.diretor, f.elenco, f.avaliacao, f.votos)

# Busca melhores do ano
lista = banco.buscar_melhores_do_ano('2019')
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.genero, f.duracao,
          f.pais, f.diretor, f.elenco, f.avaliacao, f.votos)


banco.exportar_filmes('saida.txt')
