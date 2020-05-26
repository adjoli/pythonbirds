class Pessoa:
    """Implementação de uma classe que modela uma pessoa"""

    temDeficiencia = False    # atributo de classe

    def __init__(self, *filhos, nome=None, idade=0):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"Ola {id(self)}"

    def __repr__(self):
        txtSaida = f"Meu nome é {self.nome} e tenho {self.idade} anos"

        if self.filhos:
            txtSaida = txtSaida + f"\nTenho {len(self.filhos)} filhos:"
            for filho in self.filhos:
                txtSaida = txtSaida + f"\n==> {filho}"

        return txtSaida


if __name__ == '__main__':
    filhos = [('Arthur', 7), ('Alice', 0)]

    pai = Pessoa(nome='Adao Oliveira', idade=41)
    mae = Pessoa(nome='Poliana Carlos', idade=39)

    for filho in filhos:
        pai.filhos.append(Pessoa(nome=filho[0], idade=filho[1]))

    print(pai)

    # O atributo __dict__ lista todos os atributos de instancia de um objeto.

    # Imprimindo o objeto ANTES da criacao de um atributo de instancia
    print(pai.__dict__)

    # Criando um atributo booleano 'casado' no objeto 'pai'
    # (esse atributo nao existe em outros objetos da classe Pessoa
    pai.casado = True

    # Imprimindo novamente os atributos de instancia
    print(pai.__dict__)

    mae.filhos = pai.filhos.copy()
    mae.temDeficiencia = True
    print(mae)

    print(pai.__dict__)
    print(mae.__dict__)

    # teste
    print(pai.temDeficiencia)
    print(mae.temDeficiencia)


