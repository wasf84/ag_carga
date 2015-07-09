# -*- coding: utf-8 -*-

__author__ = 'Mirele'

from base.ag import *

def main():
    """
    Método de inicialização da aplicação.
    Criado desta forma apenas para facilitar a leitura do código.
    """

    ag_mirele = AG()
    # melhor = ag_mirele.selecionarMelhorPopulacao(ag_mirele.populacao)
    # melhor.printIndividuo()

    # quantas vezes o AG vai ser executado para tentar convergir para o resultado otimo (local ou global, tanto faz...)
    maxIter = 30

    i = 0
    while i < maxIter:
        ag_mirele.pareamento()
        i =+ 1


# ------------------------------- #
# ------------------------------- #
# ----- Inicio da aplicacao ----- #
# ------------------------------- #
# ------------------------------- #
if __name__ == '__main__':
    main()
