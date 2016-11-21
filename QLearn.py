from Helpers import *



def initQMatrix(initialState):
    abilities = initialState.abilities
    print('yes')

    Qmatrix = []

    for ability in abilities:
        listy = []
        for ability2 in abilities:
            listy.append(0)
        Qmatrix.append(listy)

    print(Qmatrix)







def main():
    initialstate = CreateInitialState()
    initQMatrix(initialstate)

main()
