from black import main


class Pessoa:
    def cunprimentar(self):
        return f"Olá, {id(self)}"


if __name__ == "__main__":
    p = Pessoa()
    print(p.cunprimentar())
