# -*- coding: utf-8 -*-

__author__ = 'Mirele'

from individuo import *

class AG:
    """
    Atributos da classe:
    -   geracao     : inteiro
    -   populacao[] : vetor de objetos Individuo.
    """

    # ------------------------------------ #
    def __init__(self):
        """
        Vai gerar a populacao inicial aqui dentro.
        Sempre 16 individuos.
        """

        # Inicializacao dos atributos da classe
        self.geracao = None
        self.populacao = []

        self.geracao = 1
        for i in range(0, 16):
            ind = Individuo()
            self.populacao.append(ind)
    # ------------------------------------ #

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

    # ------------------------------------ #
    def selecionarMelhorPopulacao(self, lista = None):
        # Primeiro eu pego os individuos que estao dentro do limite de carga do aviao (5 toneladas).
        listaMelhores = []
        for i in range(0, len(lista)):
            if lista[i].retornaCargaTotal() <= 5:
                listaMelhores.append(lista[i])

        # Agora pego quem tiver a maior utilidade.
        # Comeco supondo que o primeiro individuo que eh o melhor.
        melhor = listaMelhores[0]

        for i in range(1, len(listaMelhores)):
            if listaMelhores[i].retornaUtilidade() > melhor.retornaUtilidade():
                melhor = listaMelhores[i]

        return melhor
    # ------------------------------------ #

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
        elif (individuo1.retornaCargaTotal() > 5) and (individuo2.retornaCargaTotal() <= 5):
            return individuo2
        else:
            # Pode acontecer que nenhum dos dois testados esteja dentro do limite da carga.
            # Sendo assim, eu escolho o "menos pior", o que estah mais perto do limite da carga de 5T.
            if individuo1.retornaCargaTotal() < individuo2.retornaCargaTotal():
                return individuo1
            elif individuo2.retornaCargaTotal() < individuo1.retornaCargaTotal():
                return individuo2
            else:
                # Coincidentemente, ambos tem o mesmo valor de carga. Deliberadamente escolho um deles.
                return individuo1
    # ------------------------------------ #

    # ------------------------------------ #
    def pareamento(self, index):
        """
        :param index:
        :return: o melhor individuo da populacao de filhos pareados.
        """

        # A nova populacao
        novaPopulacao = []

        # Individuos gerados do pareamento.
        lstIndividuos = []

        while len(novaPopulacao) < 16:
            for i in range(0, 16):
                if index != i:
                    parente1 = self.populacao[index]
                    parente2 = self.populacao[i]
                    cromoFilho1 = parente1.cromossomo[0:4]
                    cromoFilho1 += parente2.cromossomo[4:8]
                    filho1 = Individuo(cromoFilho1)
                    cromoFilho2 = parente2.cromossomo[0:4]
                    cromoFilho2 += parente1.cromossomo[4:8]
                    filho2 = Individuo(cromoFilho2)
                    melhor = self.escolherMelhor(filho1, filho2)

                    # Nesta lista vai ficando apenas os melhores filhos gerados.
                    lstIndividuos.append(melhor)

    # ------------------------------------ #