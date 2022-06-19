class Carro:
    def __init__(self, velocidade=0, indice_cardinal=0):
        self.motor = Motor(velocidade)
        self.direcao = Direcao(indice_cardinal)

    def velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        """>>> carro = Carro()
        >>> carro.velocidade()
        0
        >>> carro.acelerar()
        >>> carro.velocidade()
        1
        >>> carro.acelerar()
        >>> carro.velocidade()
        2
        >>> carro.acelerar()
        >>> carro.velocidade()
        3"""

        self.motor.acelerar()

    def frear(self):
        """>>> carro = Carro(velocidade=5)
        >>> carro.velocidade()
        5
        >>> carro.frear()
        >>> carro.velocidade()
        3
        >>> carro.frear()
        >>> carro.velocidade()
        1
        >>> carro.frear()
        >>> carro.velocidade()
        0
        """

        self.motor.frear()

    def compasso(self):
        return self.direcao.cardinal

    def girar_a_direita(self):
        """>>> carro = Carro()
        >>> carro.compasso()
        'Norte'
        >>> carro.girar_a_direita()
        >>> carro.compasso()
        'Leste'
        >>> carro.girar_a_direita()
        >>> carro.compasso()
        'Sul'
        >>> carro.girar_a_direita()
        >>> carro.compasso()
        'Oeste'
        >>> carro.girar_a_direita()
        >>> carro.compasso()
        'Norte'
        """

        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        """>>> carro = Carro()
        >>> carro.girar_a_esquerda()
        >>> carro.compasso()
        'Oeste'
        >>> carro.girar_a_esquerda()
        >>> carro.compasso()
        'Sul'
        >>> carro.girar_a_esquerda()
        >>> carro.compasso()
        'Leste'
        >>> carro.girar_a_esquerda()
        >>> carro.compasso()
        'Norte'
        """

        self.direcao.girar_a_esquerda()


class Motor:
    """Controla e apresenta a velocidade do Carro.
    Acrescente parâmetro de velocidade opcional. Padrão: velocidade = 0
    """

    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def velocimetro(self):
        """Retorna o valo da velocidade atual."""
        return self.velocidade

    def acelerar(self):
        """Incrementa velocidade em uma unidade.
        >>> motor = Motor()
        >>> motor.velocimetro()
        0
        >>> motor.acelerar()
        >>> motor.velocimetro()
        1
        >>> motor.acelerar()
        >>> motor.velocimetro()
        2
        >>> motor.acelerar()
        >>> motor.velocimetro()
        3
        """
        self.velocidade += 1

    def frear(self):
        """Decrementa o compasso da velocidade em duas unidades até o compasso
        limite de zero.
        >>> motor = Motor(velocidade=5)
        >>> motor.velocimetro()
        5
        >>> motor.frear()
        >>> motor.velocimetro()
        3
        >>> motor.frear()
        >>> motor.velocimetro()
        1
        >>> motor.frear()
        >>> motor.velocimetro()
        0
        """

        if self.velocidade < 2:
            self.velocidade = 0
        else:
            self.velocidade -= 2


class Direcao:
    """Controla e apresenta a direção do Carro.
    Acrescente parâmetro de direção opcional. Padrão: cardinal = 0

    0 -> Norte,  1 -> Leste,  2 -> Sul,  3 -> Oeste.


    """

    def __init__(self, indice_cardinal=0):
        self.cardinais = ("Norte", "Leste", "Sul", "Oeste")
        self.indice_cardinal = indice_cardinal
        self.cardinal = self.cardinais[indice_cardinal]

    def compasso(self):
        """Retorna cardinal."""
        return self.cardinal

    def girar(self, volta):
        self.indice_cardinal += volta
        self.cardinal = self.cardinais[self.indice_cardinal]
        return self.cardinal

    def girar_a_direita(self):
        """>>> direcao = Direcao()
        >>> direcao.compasso()
        'Norte'
        >>> direcao.girar_a_direita()
        >>> direcao.compasso()
        'Leste'
        >>> direcao.girar_a_direita()
        >>> direcao.compasso()
        'Sul'
        >>> direcao.girar_a_direita()
        >>> direcao.compasso()
        'Oeste'
        >>> direcao.girar_a_direita()
        >>> direcao.compasso()
        'Norte'
        """

        if self.indice_cardinal == len(self.cardinais) - 1:
            self.indice_cardinal = 0
            self.cardinal = self.cardinais[self.indice_cardinal]
        else:
            self.girar(1)

    def girar_a_esquerda(self):
        """>>> direcao = Direcao()
        >>> direcao.girar_a_esquerda()
        >>> direcao.compasso()
        'Oeste'
        >>> direcao.girar_a_esquerda()
        >>> direcao.compasso()
        'Sul'
        >>> direcao.girar_a_esquerda()
        >>> direcao.compasso()
        'Leste'
        >>> direcao.girar_a_esquerda()
        >>> direcao.compasso()
        'Norte'
        >>> direcao.girar_a_esquerda()
        >>> direcao.compasso()
        'Oeste'
        """
        if self.indice_cardinal == 0:
            self.indice_cardinal = len(self.cardinais) - 1
            self.cardinal = self.cardinais[self.indice_cardinal]
        else:
            self.girar(-1)
