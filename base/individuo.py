# -*- coding: utf-8 -*-

__author__ = 'Mirele'

from random import randint

class Individuo:
    cromossomo = []
    utilidade = None
    carga = None

    # ------------------------------------ #
    def __init__(self):
        # Gerando uma lista binaria aleatoria
        # fonte: <http://code.activestate.com/recipes/577944-random-binary-list/>
        randBinList = lambda n: [randint(0, 1) for b in range(1, n+1)]

        self.cromossomo = randBinList(8)
        self.calcularUtilidade()
        self.calcularCargaTotal()
        # self.printIndividuo()

    # ------------------------------------ #
    def calcularUtilidade(self):
        """
        Funcao de Avaliacao (conceito geral de AG) que calcularah a utilidade do individuo em questao
        """

        # Pegando a quantidade de Item_1
        x1 = 0
        for i in range(0, 5):
            x1 = x1 + self.cromossomo[i]

        # Pegando a quantidade de Item_2
        x2 = self.cromossomo[5]

        # Pegando a quantidade de Item_3
        x3 = 0
        for i in range(6, 8):
            x3 = x3 + self.cromossomo[i]

        self.utilidade = 9*x1 + 27*x2 + 20*x3

    # ------------------------------------ #
    def calcularCargaTotal(self):
        """
        Funcao para calcular a carga total do individuo em questao.
        """

        # Pegando a quantidade de Item_1
        x1 = 0
        for i in range(0, 5):
            x1 = x1 + self.cromossomo[i]

        # Pegando a quantidade de Item_2
        x2 = self.cromossomo[5]

        # Pegando a quantidade de Item_3
        x3 = 0
        for i in range(6, 8):
            x3 = x3 + self.cromossomo[i]

        self.carga = 1*x1 + 3*x2 + 2*x3

    # ------------------------------------ #
    def retornaUtilidade(self):
        return self.utilidade

    # ------------------------------------ #
    def retornaCargaTotal(self):
        return self.carga

    # ------------------------------------ #
    def printIndividuo(self):
        print "Cromossomo: " + str(self.cromossomo)
        print "Utilidade: " + str(self.utilidade)
        print "Carga Total: " + str(self.carga)
