""" Main algorithm implementation """

from Helpers import *

def main():
    r_matrix = {}
    q_matrix = {}
    
    initial = CreateInitialState()
    r_matrix[initial] = convertState(initial)
    print(r_matrix)

    second = ConstructNextState(initial, "mortal_strike")
    print(convertState(second))
    
main()
