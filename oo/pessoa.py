class Pessoa:
    olhos = 2

    def __init__(self, nome, idade=None, *filhos):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"Olá, {self.nome}"

    def biografia(self):
        print(f"Nome: [{self.nome}]")
        print(f"Idade: [{self.idade}]")
        print("Filhos: ", end="")
        for filho in self.filhos:
            print(f"[{filho}] ", end="")
        print("")


if __name__ == "__main__":
    felipe = Pessoa("Felipe", 35, *["Nina", "Mel"])
    print(felipe.cumprimentar())
    felipe.biografia()
    print(f"ID de Felipe: {id(felipe.olhos)}")
    print(f"ID de Pessoa: {id(Pessoa.olhos)}")
