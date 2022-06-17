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
