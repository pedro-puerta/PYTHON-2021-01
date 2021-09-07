'''
Implemente as classes Pessoa e Aluno.
A classe Pessoa deve armazenar o nome da pessoa.
A classe Aluno deve herdar da classe Pessoa e armazena o ra e uma lista
com as notas de 5 atividades realizadas durante o semestre.
Os atributos das classes devem ser inicializados nos construtores.
A lista de notas do aluno deve ser inicializada como vazia.
A classe Aluno deve implementar os métodos:
    cadastrar: recebe como entrada uma nota e a insere na lista de notas.
    calcular_media: retorna a média aritmética das notas do aluno. Essa
    média deve desconsiderar a nota mais baixa.
'''


# --------------------- IMPLEMENTE SEU CÓDIGO AQUI --------------------------
class Pessoa:
    def __init__(self, nome):
        self.nome = nome


class Aluno(Pessoa):
    def __init__(self, ra, nome):
        super().__init__(nome)
        self.ra = ra
        self.notas = []

    def cadastrar(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        self.notas.sort()
        soma = self.notas[1] + self.notas[2] + self.notas[3] + self.notas[4]
        return soma/4


# -------------- PROGRAMA PRINCIPAL (não deve ser alterado) -----------------

aluno1 = Aluno(123456, 'João')
aluno1.cadastrar(8.0)
aluno1.cadastrar(7.0)
aluno1.cadastrar(9.0)
aluno1.cadastrar(6.0)
aluno1.cadastrar(7.0)
print("Média:", aluno1.calcular_media())       # Média: 7.75

aluno2 = Aluno(123456, 'Maria')
aluno2.cadastrar(10.0)
aluno2.cadastrar(9.0)
aluno2.cadastrar(6.5)
aluno2.cadastrar(5.0)
aluno2.cadastrar(7.5)
print("Média:", aluno2.calcular_media())       # Média: 8.25
