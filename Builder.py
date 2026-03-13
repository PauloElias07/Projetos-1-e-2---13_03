#Produtos
class Pessoa:

    def __init__(self):
        self.nome = None
        self.cargo = None
        self.matricula = None
        self.horaEntrada = None
        self.horaSaida = None

    def mostrar(self):
        print("Nome:", self.nome)
        print("Cargo:", self.cargo)
        print("Matrícula:", self.matricula)
        print("Hora Entrada:", self.horaEntrada)
        print("Hora Saída:", self.horaSaida)
        print("--------------------")


#Builder
class PessoaBuilder:

    def __init__(self):
        self.pessoa = Pessoa()

    def set_nome(self, nome):
        self.pessoa.nome = nome
        return self

    def set_cargo(self, cargo):
        self.pessoa.cargo = cargo
        return self

    def set_matricula(self, matricula):
        self.pessoa.matricula = matricula
        return self

    def set_hora_entrada(self, hora):
        self.pessoa.horaEntrada = hora
        return self

    def set_hora_saida(self, hora):
        self.pessoa.horaSaida = hora
        return self

    def build(self):
        return self.pessoa


#Cricao de objetos
admin = (
    PessoaBuilder()
    .set_nome("Carlos")
    .set_cargo("Administrativo")
    .set_matricula("A123")
    .set_hora_entrada("08:00")
    .set_hora_saida("17:00")
    .build()
)

aluno = (
    PessoaBuilder()
    .set_nome("Ana")
    .set_cargo("Aluno")
    .set_matricula("2023001")
    .set_hora_entrada("07:30")
    .set_hora_saida("12:00")
    .build()
)

professor = (
    PessoaBuilder()
    .set_nome("Fernando")
    .set_cargo("Professor")
    .set_hora_entrada("07:40")
    .set_hora_saida("13:40")
    .build()
)

admin.mostrar()
aluno.mostrar()
professor.mostrar()