""" Juan Bautista Berretta and Jack Reynolds
    Test methods for all helper functions and such. """

from main import *
import time
import random

def test_probability():
    # does this feel like 15% ?
    mortal_strike = Ability("mortal_strike", 17263, None, 5, 16)
    for i in range(10):
        print(mortal_strike.useAbility(False))
        time.sleep(1)


# Quick test to make sure CDs working as should
def test_stateTransition():
    r_matrix = {}

    initial = CreateInitialState()
    r_matrix["initial"] = convertState(initial)

    second = ConstructNextState(initial, "mortal_strike")
    r_matrix["second"] = convertState(second)

    third = ConstructNextState(initial, "rend")
    r_matrix["third"] = convertState(third)

    inorder = ["initial", "second", "third"]
    for key in inorder:
        print(key)
        for k, v in r_matrix[key].items():
            print("\t " + k)


def test_colossus():
    initial = CreateInitialState()
    one = ConstructNextState(initial, "mortal_strike")
    two = ConstructNextState(one, "colossus_smash")
    three = ConstructNextState(two, "mortal_strike")


def test_state_comparison():
    initial = CreateInitialState()
    initial2 = CreateInitialState()
    print("Expected True: " + str(compareStates(initial, initial2)))

    two = ConstructNextState(initial, "colossus_smash")
    print("Expected False: " + str(compareStates(initial, two)))


def test_indexing():
    matrix = {}

    initial = CreateInitialState()
    initial2 = CreateInitialState()

    matrix[initial] = convertState(initial)

    print(getKey(matrix, initial2))


def test_update_q():
    q_matrix = {}
    r_matrix = {}
    initial_state = CreateInitialState()
    r_matrix[initial_state] = convertState(initial_state)
    next_state = ConstructNextState(initial_state, "colossus_smash")
    r_matrix[next_state] = convertState(next_state)
    update_q(q_matrix, r_matrix, .9, next_state, initial_state, "colossus_smash")
    print(q_matrix)