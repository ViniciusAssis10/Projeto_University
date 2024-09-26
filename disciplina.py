class Disciplina:
    def __init__(self, id, descricao, idCurso):
        self.id = id
        self.descricao = descricao
        self.curso = idCurso

    def imprimeDisciplina(self):
        print(f"ID: {self.id} | Descrição: {self.descricao}")

