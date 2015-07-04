# -*- coding: utf-8 -*-

__author__ = 'Mirele'

from base.ag import *

def main():
    """
    Método de inicialização da aplicação.
    Criado desta forma apenas para facilitar a leitura do código.
    """

    ag_mirele = AG()
    melhor = ag_mirele.selecionarMelhorPopulacao()
    melhor.printIndividuo()


# ------------------------------- #
# ------------------------------- #
# ----- Inicio da aplicacao ----- #
# ------------------------------- #
# ------------------------------- #
if __name__ == '__main__':
    main()
