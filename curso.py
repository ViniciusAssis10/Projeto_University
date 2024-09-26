class Curso:
    def __init__(self, id, descricao, departamento):
        self.id = id
        self.descricao = descricao
        self.departamento = departamento

    def imprimeCurso(self):
        print(f"ID: Curso: {self.id} | Nome: {self.descricao} | Departamento: {self.departamento}")
