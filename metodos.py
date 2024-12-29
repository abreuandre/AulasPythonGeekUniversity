"""
POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações
que este objeto pode realizar no seu sistema.

Em Python, dividimos os métodos, em 2 grupos: Métodos de intância
e Métodos de Classe.

# Métodos de Instância.

# O método dunder init __init__ é um método especial chamado de construtor e
sua função é construir o objeto a partir da classe.
"""

class Lampada:

    def __index__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id


class Usuario:

    def __init__(self, nome, email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha = senha
