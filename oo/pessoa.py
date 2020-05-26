class Pessoa:
    def __init__(self, nome=None, idade=41):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f"Ola {id(self)}"

    def __repr__(self):
        return f"{self.nome} tem {self.idade} anos"


if __name__ == '__main__':
    p1 = Pessoa('Xico')
    p2 = Pessoa('Arthur', 7)
    print(Pessoa.cumprimentar(p1))
    print(p1.cumprimentar())
    print(id(p1))

    print(p1)
    print(p2)
