class Pessoa:
    def __init__(self, nome, idade=None):
        self.nome = nome
        self.idade = idade

    def cunprimentar(self):
        return f"Olá, {self.nome}"


if __name__ == "__main__":
    p = Pessoa("Felipe")
    print(p.cunprimentar())
