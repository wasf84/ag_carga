# -*- coding: utf-8 -*-

__author__ = 'Mirele'

from individuo import *

class AG:
    geracao = None
    populacao = []

    def __init__(self):
        """
        Vai gerar a populacao inicial aqui dentro.
        """

        self.geracao = 1
        for i in range(0, 16):
            ind = Individuo()
            self.populacao.append(ind)

    def printTudo(self):
        """
        Imprime tudo que contiver no AG
        """

        print "Geracao: " + str(self.geracao)
        for i in range(0, len(self.populacao)):
            print "x ---------------------- x"
            print "ID: " + str(i+1)
            self.populacao[i].printIndividuo()