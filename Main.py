""" Main algorithm implementation """
import time
from helpers import *

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

# updates the q matrix with the corresponding reward     
def update_q(q_matrix, r_matrix, gamma, next_state, current_state, chosen_action):
    # Begin by finding the highest value of the next state in the q matrix
    # If Q(next_state) doesn't exist then the reward is just 0
    ns_actions = getKey(q_matrix, next_state)
    if (q_ns == None):
        ns_reward = 0
    else:
        # choose the action that yields the highest reward
        ns_max_value = 0
        ns_max_ability = "not set"
        for key, value in ns_actions.items():
            if value > ns_max:p
                ns_max_value = value
                ns_max_ability = key
        ns_reward = ns_max_value
        print("The best ability for the next state is: " + key + "\nWith a value of: " str(value))

    # Get reward of of current state
    cs_actions = getKey(r_matrix, chosen_action)
    cs_reward = cs_actions[chosen_action]

    # Compute the reward for the Q matrix
    q_reward = cs_reward + gamma * ns_reward
    q_matrix[current_state] = {chosen_action:q_reward}

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
            chosen_action = choices[random_index]
            next_state = ConstructNextState(current_state, chosen_action)

            # Update target health
            target = next_state.target.health

            # Add to reward matrix
            r_matrix[next_state] = convertState(next_state)

            # Q(state, action) = R(state, action) + Gamma * Max[Q(next state, all actions)]
            update_q(q_matrix, r_matrix, gamma, next_state, current_state, chosen_action)
            current_state = next_state

        
def main():
    """ Tests """
    #test_indexing()
    #test_stateTransition()
    test_colossus()
    #test_state_comparison()

main()
