from .Helpers import Helpers



def initQMatrix(initialState):
    abilities = initialState.abilities

    Qmatrix = []

    for ability in abilities:
        listy = []
        for ability2 in abilities:
            listy.append(0)
        Qmatrix.append(listy)

    print(Qmatrix)







def main():
    CreateInitialState()

