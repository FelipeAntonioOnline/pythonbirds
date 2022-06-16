class Pessoa:
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


if __name__ == "__main__":
    felipe = Pessoa("Felipe", 35, *["Nina", "Mel"])
    print(felipe.cumprimentar())
    felipe.biografia()
