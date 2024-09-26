class Professor:
    def __init__(self, bi, nome, idDisciplina):
        self.bi = bi
        self.nome = nome
        self.disciplina = idDisciplina


    def infoCurso(self):
        self.disciplina.imprimeDisciplina()
        print(f"Nome do Professor da disciplina: {self.nome}")