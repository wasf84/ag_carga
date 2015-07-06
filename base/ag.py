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
        Sempre 16 individuos.
        """

        self.geracao = 1
        for i in range(0, 16):
            ind = Individuo()
            self.populacao.append(ind)

    # ------------------------------------ #
    def printTudo(self):
        """
        Imprime tudo que contiver no AG

        :return: dados no console (pode ser modificado para imprimir num arquivo de texto).
        """

        print "Geracao: " + str(self.geracao)
        for i in range(0, len(self.populacao)):
            print "x ---------------------- x"
            print "ID: " + str(i)
            self.populacao[i].printIndividuo()

    # ------------------------------------ #
    def printUmEspecifico(self, index):
        """
        Imprime um unico individuo da populacao.

        :param index: posicao do individuo no vetor populacao.
        :return: dados no console (pode ser modificado para imprimir num arquivo de texto).
        """
        # print "Geracao: " + str(self.geracao)
        if index in range(0, len(self.populacao)):
            print "x ---------------------- x"
            print "ID: " + str(index)
            self.populacao[index].printIndividuo()
            print "x ---------------------- x"

    # ------------------------------------ #
    def selecionarMelhorPopulacao(self):
        # Primeiro eu pego os individuos que estao dentro do limite de carga do aviao (5 toneladas).
        listaMelhores = []
        for i in range(0, len(self.populacao)):
            if self.populacao[i].retornaCargaTotal() <= 5:
                listaMelhores.append(self.populacao[i])

        # Agora pego quem tiver a maior utilidade.
        # Comeco supondo que o primeiro individuo que eh o melhor.
        melhor = listaMelhores[0]

        for i in range(1, len(listaMelhores)):
            if listaMelhores[i].retornaUtilidade() > melhor.retornaUtilidade():
                melhor = listaMelhores[i]

        return melhor

    # ------------------------------------ #
    def escolherMelhor(self, individuo1, individuo2):
        """
        Usar este metodo sempre apos o pareamento entre 2 cromossomos, para escolher o melhor filho gerado.
        Caso ambos tenham a mesma utilidade e estejam dentro do limite de carga, nao faz distincao entre eles e retorna
            direto o primeiro filho.

        :param individuo1: primeiro objeto individuo gerado apos o pareamento
        :param individuo2: segundo objeto individuo gerado apos o pareamento
        :return: retornarah o objeto individuo que tiver maior utilidade dentro do limite da carga total
        """

        # Verifico se ambos estao dentro do limte da carga total (<= 5T)
        if (individuo1.retornaCargaTotal() <= 5) and (individuo2.retornaCargaTotal() <= 5):
            # Agora pega qual tem maior UTILIDADE
            if individuo1.retornaUtilidade() >= individuo2.retornaUtilidade():
                return individuo1
            else:
                return individuo2
        # O individuo 1 estah dentro do limite mas o individuo 2 nao.
        elif (individuo1.retornaCargaTotal() <= 5) and (individuo2.retornaCargaTotal() > 5):
            return individuo1
        # O individuo 2 estah dentro do limite mas o individuo 1 nao.
        else:
            return individuo2

    # ------------------------------------ #
    def pareamento(self, index):
        """

        :param index:
        :return:
        """
