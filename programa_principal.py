# Pedro Silverio Puerta
# Adalto de Almeida Linhares Santos


from classes import (Aluno, Instrutor, Turma, Atividade)


# Criando os Alunos:
aluno0 = Aluno('123456-7', 'Pedro', '11-04-1999',
               '+55 11 99889-6547', 1, '30-04-2021', 1.75, 60.1)
aluno1 = Aluno('654321-x', 'Adalto', '01-05-1995',
               '+55 11 96854-6547', 2, '30-04-2021', 1.80, 70.1)
aluno2 = Aluno('789456-8', 'Emma', '03-12-1992',
               '+55 11 96325-6547', 3, '30-04-2021', 1.60, 80.1)
aluno3 = Aluno('258369-1', 'João', '18-03-1998',
               '+55 11 91547-6547', 4, '30-04-2021', 1.81, 90.1)
aluno4 = Aluno('147852-y', 'Gustavo', '30-04-1999',
               '+55 11 95864-6547', 5, '30-04-2021', 1.73, 60.1)
aluno5 = Aluno('738691-4', 'Davi', '06-04-2000',
               '+55 11 92568-6547', 6, '30-04-2021', 1.74, 70.1)
aluno6 = Aluno('951488-2', 'Ana', '25-03-2001',
               '+55 11 97584-6547', 7, '30-04-2021', 1.70, 80.1)
aluno7 = Aluno('263119-7', 'Mariana', '21-01-1997',
               '+55 11 93684-6547', 8, '30-04-2021', 1.74, 90.1)
aluno8 = Aluno('778899-7', 'Gabriela', '02-06-1990',
               '+55 11 99487-6547', 9, '30-04-2021', 1.75, 60.1)
aluno9 = Aluno('747578-7', 'Jonas', '23-07-1994',
               '+55 11 99654-6547', 10, '30-04-2021', 1.90, 100.1)

# Incluíndo Faltas:
aluno0.set_faltas(3)
aluno0.set_faltas(1)
aluno2.set_faltas(2)
aluno2.set_faltas(1)
aluno4.set_faltas(3)
aluno4.set_faltas(6)
aluno6.set_faltas(7)
aluno6.set_faltas(1)
aluno8.set_faltas(1)
aluno8.set_faltas(3)

# Criando Monitor:
aluno1.set_monitor(True)
aluno3.set_monitor(True)
aluno5.set_monitor(True)
aluno7.set_monitor(True)
aluno9.set_monitor(True)

# Exibando dados dos Alunos:
aluno0.exibir()
aluno1.exibir()
aluno2.exibir()
aluno3.exibir()
aluno4.exibir()
aluno5.exibir()
aluno6.exibir()
aluno7.exibir()
aluno8.exibir()
aluno9.exibir()

# Criando Instrutores:
instrutor0 = Instrutor('159331-7', 'Roberto', '05-01-1980',
                       '+55 11 99887-1122', 'Personal Trainer')
instrutor1 = Instrutor('556616-7', 'Luis', '06-09-1992',
                       '+55 11 95144-1122', 'Personal Trainer')
instrutor2 = Instrutor('119915-7', 'Brian', '25-12-1994',
                       '+55 11 92166-1122', 'Professor de Zumba')
instrutor3 = Instrutor('336675-7', 'Keila', '07-09-1990',
                       '+55 11 98744-1122', 'Professora de Ioga')

# Exibindo dados dos Instrutores:
instrutor0.exibir()
instrutor1.exibir()
instrutor2.exibir()
instrutor3.exibir()

# Criando Atividades:
atividade0 = Atividade('Zumba')
atividade1 = Atividade('Musculação')
atividade2 = Atividade('Crossfit')
atividade3 = Atividade('Ioga')

# Exibindo dados das Atividades:
atividade0.exibir()
atividade1.exibir()
atividade2.exibir()
atividade3.exibir()

# Criando Turmas:
turma0 = Turma('14:00', '01:00', '01-01-2021', '01-12-2021',
               atividade0, instrutor0)
turma1 = Turma('15:00', '01:00', '01-01-2021', '01-12-2021',
               atividade1, instrutor1)
turma2 = Turma('16:00', '01:00', '01-01-2021', '01-12-2021',
               atividade2, instrutor2)
turma3 = Turma('17:00', '01:00', '01-01-2021', '01-12-2021',
               atividade3, instrutor3)

# Incluíndo Monitores nas Turmas:
turma0.set_monitor(aluno1)
turma1.set_monitor(aluno3)
turma2.set_monitor(aluno5)
turma3.set_monitor(aluno7)

# Incluíndo Alunos nas Turmas:
turma0.inclui_aluno(aluno0)
turma0.inclui_aluno(aluno1)
turma0.inclui_aluno(aluno2)
turma1.inclui_aluno(aluno3)
turma1.inclui_aluno(aluno4)
turma1.inclui_aluno(aluno5)
turma2.inclui_aluno(aluno6)
turma2.inclui_aluno(aluno7)
turma3.inclui_aluno(aluno8)
turma3.inclui_aluno(aluno9)

# Alterando Instrutor:
turma0.alterar_instrutor(instrutor1)

# Exibando dados das Turmas:
turma0.exibir()
turma1.exibir()
turma2.exibir()
turma3.exibir()
