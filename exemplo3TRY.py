# cadastrar em um dicionario 3 alunos
# chave é o ra
# valor é o nome
# não deve permitir ras iguais


alunos = {}
while len(alunos) < 3:
    try:
        ra = int(input("RA: "))
        nome = input("Nome: ")
        if ra in alunos:
            raise KeyError
        else:
            alunos[ra] = nome
    except KeyError:
        print("O RA já esta cadastrado. Digite os dados novamente")
    except ValueError:
        print("Valor informado no formato invalido")

print(alunos)
