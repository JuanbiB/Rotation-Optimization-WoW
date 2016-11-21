from Helpers import *

import random



def initQMatrix(initialState):
    abilities = initialState.abilities
    #print('yes')

    Qmatrix = []

    for ability in abilities:
        listy = []
        for ability2 in abilities:
            listy.append(0)
        Qmatrix.append(listy)

    return Qmatrix


#def MatrixR(initialState):






def main():
    initialstate = CreateInitialState()
    Qmatrix =  initQMatrix(initialstate)

    gamma = random.random()


main()
