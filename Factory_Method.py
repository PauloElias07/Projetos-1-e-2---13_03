from abc import ABC, abstractmethod

# Classe abstrata
class Pessoa(ABC):
    
    @abstractmethod
    def tipo(self):
        pass


# Classes concretas
class Administrativo(Pessoa):
    def tipo(self):
        return "Pessoa do tipo Administrativo"


class Aluno(Pessoa):
    def tipo(self):
        return "Pessoa do tipo Aluno"


class Professor(Pessoa):
    def tipo(self):
        return "Pessoa do tipo Professor"


class Publico(Pessoa):
    def tipo(self):
        return "Pessoa do tipo Público"


#FactoryMethod
class PessoaFactory:

    @staticmethod
    def criar_pessoa(tipo):
        if tipo == "administrativo":
            return Administrativo()
        elif tipo == "aluno":
            return Aluno()
        elif tipo == "professor":
            return Professor()
        elif tipo == "publico":
            return Publico()
        else:
            raise ValueError("Tipo de pessoa inválido")


#Usabilidade
p1 = PessoaFactory.criar_pessoa("aluno")
p2 = PessoaFactory.criar_pessoa("professor")
p3 = PessoaFactory.criar_pessoa("administrativo")

print(p1.tipo())
print(p2.tipo())
print(p3.tipo())
