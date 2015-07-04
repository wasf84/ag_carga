# -*- coding: utf-8 -*-

__author__ = 'Mirele'

from individuo import *

class AG:
    geracao = None
    populacao = []

    # ------------------------------------ #
    def __init__(self):
        """
        Vai gerar a populacao inicial aqui dentro.
        """

        self.geracao = 1
        for i in range(0, 16):
            ind = Individuo()
            self.populacao.append(ind)

    # ------------------------------------ #
    def printTudo(self):
        """
        Imprime tudo que contiver no AG
        """

        print "Geracao: " + str(self.geracao)
        for i in range(0, len(self.populacao)):
            print "x ---------------------- x"
            print "ID: " + str(i)
            self.populacao[i].printIndividuo()

    # ------------------------------------ #
    def printUmEspecifico(self, index):
        # print "Geracao: " + str(self.geracao)
        if index in range(0, len(self.populacao)):
            print "x ---------------------- x"
            print "ID: " + str(index)
            self.populacao[index].printIndividuo()
            print "x ---------------------- x"

    # ------------------------------------ #
    def selecionarMelhorPopulacao(self):
        # Primeiro eu pego os individuos que estao dentro do limite de carga do aviao, que eh de 5 toneladas.
        listaMelhores = []
        for i in range(0, len(self.populacao)):
            if self.populacao[i].retornaCargaTotal() <= 5:
                listaMelhores.append(self.populacao[i])

        # Agora pego quem tiver a maior utilidade.
        melhor = listaMelhores[0]

        for i in range(1, len(listaMelhores)):
            if listaMelhores[i].retornaUtilidade() > melhor.retornaUtilidade():
                melhor = listaMelhores[i]

        return melhor
