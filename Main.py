""" Main algorithm implementation """
import time
from Helpers import *

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
    dict = {}
    
    initial = CreateInitialState()
    initial2 = CreateInitialState()

    dict[initial] = convertState(initial)

    print(getKey(dict, initial2))

def q_learn(episodes):
    """ Q-Learning Algorithm """
    gamma = 0.9

    # doing 10 episodes for now 
    for i in range(episodes):
        # We know what state we're starting at, so no need to select a random one
        initial_state = CreateInitialState()
        target = initial_state.target
        
        r_matrix = {initial_state}
        q_matrix = {}

        current_state = initial_state
        # one episode = one depletion 
        while (target > 0):
            # select a random action to take
            choices = list(getKey(r_matrix, current_state).keys())
            c_length = len(choices)
            random_index = random.randint(0, c_length - 1) # or not - 1?
            # Construct next state by choosing random action
            next_state = ConstructNextState(current_state, choices[random_index])
            # Add to reward matrix
            r_matrix[next_state] = convertState(next_state)

            # Q(state, action) = R(state, action) + Gamma * Max[Q(next state, all actions)]
            

        
def main():
    """ Tests """
    test_indexing()
    #test_stateTransition()
    #test_colossus()
    #test_state_comparison()



        
    
main()
