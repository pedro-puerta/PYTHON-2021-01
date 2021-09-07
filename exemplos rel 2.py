'''
|-------------------|           |-------------------|
| Cachorro          |           | Pessoa            |
|-------------------|           |-------------------|
| nome              |           | nome              |
| idade             |-----------| sobrenome         |
| proprietario      |           |                   |
|-------------------|           |-------------------|
|                   |           |                   |
|-------------------|           |-------------------|
'''


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


class Cachorro:
    def __init__(self, nome, idade, proprietario):
        self.nome = nome
        self.idade = idade
        self.proprietario = proprietario


pessoa1 = Pessoa('Paulo', 'Vieira')
dog = Cachorro('Rex', 2, pessoa1)
print(dog.nome)
print(dog.proprietario.nome, dog.proprietario.sobrenome)
