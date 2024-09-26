class Estudante:
    def __init__(self, bi, nome, idMatricula, idCurso):
        self.bi = bi
        self.nome = nome
        self.matricula = idMatricula
        self.curso = idCurso

    def imprimeAluno(self):
        print(f"BI: {self.bi} | Nome: {self.nome} | Matricula: {self.matricula}")