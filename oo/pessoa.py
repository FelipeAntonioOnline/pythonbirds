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

    @staticmethod
    def hitchhiker_method():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f"{cls} - olhos {cls.olhos}"


class Homem(Pessoa):
    pass


class Mutante(Pessoa):
    olhos = 1


if __name__ == "__main__":
    felipe = Pessoa("Felipe", 35, *["Nina", "Mel"])
    print(felipe.cumprimentar())
    felipe.biografia()
    print(f"ID de Felipe: {id(felipe.olhos)}")
    print(f"ID de Pessoa: {id(Pessoa.olhos)}")
    print(felipe.hitchhiker_method())
    print(felipe.nome_e_atributos_de_classe())

    pessoa = Pessoa("Anônimo")
    homem = Homem("Genérico")
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(homem, Pessoa))
    print(isinstance(homem, Homem))

    filepe = Mutante("Filepe")
    print(filepe.olhos)
