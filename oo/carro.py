# TODO Tarefa
# Criar uma classe carro que vai possuir dois atributos compostos por outras
# duas classes:
#
# 1 - Motor
# 2 - Direção
#
# O Motor terá a responsabilidade de contrololar a velocidade. Ele oferece os
# seguintes atributos:
# a) Atributo de dado velocidade
# b) Método acelerar, que deverá incrementar a velocidade de uma unidade.
# c) Método frear que deverá decrementar a velocidade em duas unidades.
#
# A Direção terá a responsabilidade de controlar a direção. Ela oferece os
# seguintes atributos:
# a) Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste.
# b) Método girar_a_direita (sentido horário).
# c) Método girar_a_esquerda (sentido antihorário).

# Comportamento esperado
#
# >>> motor = Motor()
# >>> motor.velocidade()
# 0
# >>> motor.acelerar()
# >>> motor.velocidade()
# 1
# >>> motor.acelerar()
# >>> motor.velocidade()
# 2
# >>> motor.acelerar()
# >>> motor.velocidade()
# 3
# >>> motor.frear()
# >>> motor.velocidade()
# 1
# >>> motor.frear()
# >>> motor.velocidade()
# 0

# >>> direcao = Direcao()
# >>> direcao.valor()
# 'Norte'
# >>> direcao.gira_a_direita()
# >>> direcao.valor()
# 'Leste'
# >>> direcao.gira_a_direita()
# >>> direcao.valor()
# 'Sul'
# >>> direcao.gira_a_direita()
# >>> direcao.valor()
# 'Oeste'
# >>> direcao.gira_a_direita()
# >>> direcao.valor()
# 'Norte'

# >>> direcao.gira_a_esquerda()
# >>> direcao.valor()
# 'Oeste'
# >>> direcao.gira_a_esquerda()
# >>> direcao.valor()
# 'Sul'
# >>> direcao.gira_a_esquerda()
# >>> direcao.valor()
# 'Leste'
# >>> direcao.gira_a_esquerda()
# >>> direcao.valor()
# 'Norte'

# >>> carro = Carro()
# >>> carro.velocidade()
# 0
# >>> carro.acelerar()
# >>> carro.velocidade()
# 1
# >>> carro.acelerar()
# >>> carro.velocidade()
# 2
# >>> carro.acelerar()
# >>> carro.velocidade()
# 3
# >>> carro.frear()
# >>> carro.velocidade()
# 1
# >>> carro.frear()
# >>> carro.velocidade()
# 0

# >>> carro.valor()
# 'Norte'
# >>> carro.gira_a_direita()
# >>> carro.valor()
# 'Leste'
# >>> carro.gira_a_direita()
# >>> carro.valor()
# 'Sul'
# >>> carro.gira_a_direita()
# >>> carro.valor()
# 'Oeste'
# >>> carro.gira_a_direita()
# >>> carro.valor()
# 'Norte'

# >>> carro.gira_a_esquerda()
# >>> carro.valor()
# 'Oeste'
# >>> carro.gira_a_esquerda()
# >>> carro.valor()
# 'Sul'
# >>> carro.gira_a_esquerda()
# >>> carro.valor()
# 'Leste'
# >>> carro.gira_a_esquerda()
# >>> carro.valor()
# 'Norte'


class Carro:
    def __init__(self):
        self.motor = Motor()
        self.direcao = Direcao()

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def valor(self):
        self.direcao.compasso()

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
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
        """Incrementa velocidade em uma unidade."""
        self.velocidade += 1

    def frear(self):
        """Decrementa o valor da velocidade em duas unidades até o valor
        limite de zero."""
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
        if self.indice_cardinal == len(self.cardinais) - 1:
            self.indice_cardinal = 0
            self.cardinal = self.cardinais[self.indice_cardinal]
        else:
            self.girar(1)

    def girar_a_esquerda(self):
        if self.indice_cardinal == 0:
            self.indice_cardinal = len(self.cardinais) - 1
            self.cardinal = self.cardinais[self.indice_cardinal]
        else:
            self.girar(-1)
