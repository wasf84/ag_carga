# -*- coding: utf-8 -*-

__author__ = 'Mirele'

from base.ag import *

# ------------------------------- #
def main():
    """
    Método de inicialização da aplicação.
    Criado desta forma apenas para facilitar a leitura do código.
    """

    ag_mirele = AG()
    ag_mirele.printTudo("ger" + str(ag_mirele.geracao))
    # melhor = ag_mirele.selecionarMelhorPopulacao(ag_mirele.populacao)
    # melhor.printIndividuo()

    # quantas vezes o AG vai ser executado para tentar convergir para o resultado otimo (local ou global, tanto faz...)
    maxGer = 200

    for i in range(0, maxGer):
        ag_mirele.executarAG()
        ag_mirele.printTudo("ger" + str(ag_mirele.geracao))
# ------------------------------- #

# ------------------------------- #
# ------------------------------- #
# ----- Inicio da aplicacao ----- #
# ------------------------------- #
# ------------------------------- #
if __name__ == '__main__':
    main()
