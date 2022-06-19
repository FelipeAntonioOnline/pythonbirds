class Carro:
    def __init__(self):
        self.motor = Motor()
        self.direcao = Direcao()

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
        """>>> carro.frear()
        >>> carro.velocidade()
        1
        >>> carro.frear()
        >>> carro.velocidade()
        0
        """

        self.motor.frear()

    def compasso(self):
        self.direcao.compasso()

    def girar_a_direita(self):
        """>>> carro.compasso()
        'Norte'
        >>> carro.gira_a_direita()
        >>> carro.compasso()
        'Leste'
        >>> carro.gira_a_direita()
        >>> carro.compasso()
        'Sul'
        >>> carro.gira_a_direita()
        >>> carro.compasso()
        'Oeste'
        >>> carro.gira_a_direita()
        >>> carro.compasso()
        'Norte'
        """

        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        """>>> carro.gira_a_esquerda()
        >>> carro.compasso()
        'Oeste'
        >>> carro.gira_a_esquerda()
        >>> carro.compasso()
        'Sul'
        >>> carro.gira_a_esquerda()
        >>> carro.compasso()
        'Leste'
        >>> carro.gira_a_esquerda()
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
        >>> motor.velocidade()
        0
        >>> motor.acelerar()
        >>> motor.velocidade()
        1
        >>> motor.acelerar()
        >>> motor.velocidade()
        2
        >>> motor.acelerar()
        >>> motor.velocidade()
        3
        """
        self.velocidade += 1

    def frear(self):
        """Decrementa o compasso da velocidade em duas unidades até o compasso
        limite de zero.
        >>> motor.frear()
        >>> motor.velocidade()
        1
        >>> motor.frear()
        >>> motor.velocidade()
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
        >>> direcao.gira_a_direita()
        >>> direcao.compasso()
        'Leste'
        >>> direcao.gira_a_direita()
        >>> direcao.compasso()
        'Sul'
        >>> direcao.gira_a_direita()
        >>> direcao.compasso()
        'Oeste'
        >>> direcao.gira_a_direita()
        >>> direcao.compasso()
        'Norte'
        """

        if self.indice_cardinal == len(self.cardinais) - 1:
            self.indice_cardinal = 0
            self.cardinal = self.cardinais[self.indice_cardinal]
        else:
            self.girar(1)

    def girar_a_esquerda(self):
        """>>> direcao.gira_a_esquerda()
        >>> direcao.compasso()
        'Oeste'
        >>> direcao.gira_a_esquerda()
        >>> direcao.compasso()
        'Sul'
        >>> direcao.gira_a_esquerda()
        >>> direcao.compasso()
        'Leste'
        >>> direcao.gira_a_esquerda()
        >>> direcao.compasso()
        'Norte'
        >>> direcao.gira_a_esquerda()
        >>> direcao.compasso()
        'Oeste'
        """
        if self.indice_cardinal == 0:
            self.indice_cardinal = len(self.cardinais) - 1
            self.cardinal = self.cardinais[self.indice_cardinal]
        else:
            self.girar(-1)
