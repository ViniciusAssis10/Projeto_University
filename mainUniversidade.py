from estudante import Estudante
from curso import Curso
from professor import Professor
from disciplina import Disciplina

op = 1

listaAlunos = []
listaCurso = []
listaDisciplinas = []
listaProfessores = []

while op != 8:
    print("Escolha uma das opções:\n"
          "1 - Registar Aluno\n"
          "2 - Registar Disciplina\n"
          "3 - Registar Curso\n"
          "4 - Registar Professor\n"
          "5 - Listar Cursos\n"
          "6 - Info Curso\n"
          "7 - Info Aluno\n"
          "8 - Sair")
    op = int(input())

    if op == 1:
        bi = str(input("Insira o BI: "))
        nome = str(input("Insira o nome do aluno: "))
        numMatri = int(input("Insira o Número da Matricula: "))
        for c in listaCurso:
            print(f"Nº Curso: {c.id} - {c.descricao}")
        curso = int(input("Insira o número do curso: "))

        course = 0
        for c in listaCurso:
            if curso == c.id:
                course = c

        listaAlunos.append(Estudante(bi, nome, numMatri, course))

        print("Aluno Inserido com sucesso!")
    elif op == 2:
        id = int(input("Insira o ID da disciplina: "))
        descricao = str(input("Insira a descrição da discplina: "))
        for c in listaCurso:
            c.imprimeCurso()
        curso = int(input("Insira o número do curso: "))

        course = 0
        for c in listaCurso:
            if curso == c.id:
                course = c

        listaDisciplinas.append(Disciplina(id, descricao, course))

        print("Disciplina Inserida com sucesso!")

    elif op == 3:
        id = int(input("Insira o ID do curso: "))
        descricao = str(input("Insira a descrição do curso: "))
        depart = str(input("Insira o Departamento: "))

        listaCurso.append(Curso(id, descricao, depart))

        print("Curso Inserido com sucesso!")

    elif op == 4:
        bi = str(input("Insira o BI: "))
        nome = str(input("Insira o nome do Professor: "))
        for d in listaDisciplinas:
            print(f"Nº Disciplina: {d.id} - {d.descricao}")
        disciplina = int(input("Insira o número do disciplina: "))
        disc = 0
        for d in listaDisciplinas:
            if d.id == disciplina:
                disc = d

        listaProfessores.append(Professor(bi, nome, disc))

        print("Professor Inserido com sucesso!")

    elif op == 5:
        for c in listaCurso:
            c.imprimeCurso()

    elif op == 6:
        for c in listaCurso:
            c.imprimeCurso()
        curso = int(input("Escolha o curso: "))

        #for disciplina in listaDisciplinas:
            #if(curso == disciplina.curso.id):
                #disciplina.infoCurso()
        print("Curso:")
        for c in listaCurso:
            if c.id == curso:
                c.imprimeCurso()

        print("Disciplinas:")
        for p in listaProfessores:
            if curso == p.disciplina.curso.id:
                p.infoCurso()
    elif op == 7:
        bi = str(input("Insira o BI: "))
        curso = 0
        
        for a in listaAlunos:
            if bi == a.bi:
                a.imprimeAluno()
                a.curso.imprimeCurso()
                curso = a.curso.id

        print("Disciplinas:")
        for p in listaProfessores:
            if curso == p.disciplina.curso.id:
                p.infoCurso()

    elif op == 8:
        print("Obrigado!")
    else:
        print("Erro! Opção Inválida")
