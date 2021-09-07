# Pedro Silverio Puerta
# Adalto de Almeida Linhares Santos


from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, rg, nome, dt_nasc, telefone):
        self.rg = rg
        self.nome = nome
        self.dt_nasc = dt_nasc
        self.telefone = telefone

    @abstractmethod
    def exibir(self):
        print('---------------------')
        print('RG:', self.rg)
        print('Nome:', self.nome)
        print('Data de Nascimento:', self.dt_nasc)
        print('Telefone:', self.telefone)


class Instrutor(Pessoa):
    def __init__(self, rg, nome, dt_nasc, telefone, titulacao):
        super().__init__(rg, nome, dt_nasc, telefone)
        self.titulacao = titulacao

    def exibir(self):
        super().exibir()
        print('Titulação:', self.titulacao)


class Aluno(Pessoa):
    def __init__(self, rg, nome, dt_nasc, telefone, id_matricula,
                 dt_matricula, altura, peso):
        super().__init__(rg, nome, dt_nasc, telefone)
        self.id_matricula = id_matricula
        self.dt_matricula = dt_matricula
        self.altura = altura
        self.peso = peso
        self.__faltas = 0
        self.__monitor = False

    def set_faltas(self, faltas):
        self.__faltas += faltas

    def get_faltas(self):
        return self.__faltas

    def set_monitor(self, boleano):
        self.__monitor = boleano

    def get_monitor(self):
        return self.__monitor

    def exibir(self):
        super().exibir()
        print('Matrícula:', self.id_matricula)
        print('Data da Matrícula:', self.dt_matricula)
        print('Altura:', self.altura)
        print('Peso:', self.peso)
        print('Faltas:', self.get_faltas())
        if self.__monitor:
            print('Aluno Monitor')
        else:
            print('Aluno não monitor')


class Atividade():
    def __init__(self, tipo):
        self.tipo = tipo

    def exibir(self):
        print('---------------------')
        print('Tipo:', self.tipo)


class Turma():
    def __init__(self, horario_aula, tempo_duracao_aula, dt_inicial,
                 dt_final, atividade, instrutor):
        self.horario_aula = horario_aula
        self.tempo_duracao_aula = tempo_duracao_aula
        self.dt_inicial = dt_inicial
        self.dt_final = dt_final
        self.atividade = atividade
        self.instrutor = instrutor
        self.__aluno_monitor = None
        self.alunos = []

    def set_monitor(self, monitor):
        if monitor.get_monitor():
            self.__aluno_monitor = monitor

    def inclui_aluno(self, aluno_incluido):
        self.alunos.append(aluno_incluido)

    def alterar_instrutor(self, novo_instrutor):
        self.instrutor = novo_instrutor

    def exibir(self):
        try:
            print('---------------------')
            print('Monitor:', self.__aluno_monitor.nome)
            print('Horário da Aula:', self.horario_aula)
            print('Tempo de duração da Aula:', self.tempo_duracao_aula)
            print('Data de início:', self.dt_inicial)
            print('Data de fim:', self.dt_final)
            print('Atividade:', self.atividade.tipo)
            print('Instrutor:', self.instrutor.nome)
            if self.alunos == []:
                print('Não há alunos na turma')
            else:
                print('Lista de alunos da turma:')
                for aluno in self.alunos:
                    print('-', aluno.nome)
            print('Quantidade de alunos:', len(self.alunos))
        except(AttributeError):
            print('Deve-se incluír um monitor para a turma!')
