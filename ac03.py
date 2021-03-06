# PROGRAMAÇÃO ORIENTADA A OBJETOS
# ATIVIDADE CONTÍNUA 03

# INSIRA ABAIXO O NOME DOS ALUNOS DO GRUPO
# ALUNO 1: Pedro Silverio Puerta
# ALUNO 2: nome
# ALUNO 3: nome
# ALUNO 4: nome
# ALUNO 5: nome
# ALUNO 6: nome


class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.casas = []

    def incluir_casa(self, Casa):
        self.casas.append(Casa)


class Casa:
    def __init__(self, nome, animal):
        self.nome = nome
        self.animal = animal
        self.diretor = None
        self.monitor = None

    def set_diretor(self, Diretor):
        self.diretor = Diretor

    def set_monitor(self, Monitor):
        self.monitor = Monitor


class Professor:
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento
        self.disciplinas = []

    def incluir_disciplina(self, Disciplina):
        self.disciplinas.append(Disciplina)


class Disciplina:
    def __init__(self, nome, ementa):
        self.nome = nome
        self.ementa = ementa
        self.alunos = []

    def incluir_aluno(self, Aluno):
        self.alunos.append(Aluno)


class Aluno:
    def __init__(self, nome, nascimento, tipo):
        self.nome = nome
        self.nascimento = nascimento
        self.tipo = tipo
        self.casa = None
        self.__triunfos = 0
        self.__mau_feitos = 0

    def set_casa(self, Casa):
        self.casa = Casa

    def incluir_triunfo(self, quantidade):
        self.__triunfos += quantidade

    def incluir_mau_feito(self, quantidade):
        self.__mau_feitos += quantidade

    def get_triunfos(self):
        return self.__triunfos

    def get_mau_feitos(self):
        return self.__mau_feitos
