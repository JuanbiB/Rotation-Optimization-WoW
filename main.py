""" Main algorithm implementation """
from helpers import *


# updates the q matrix with the corresponding reward     
def update_q(q_matrix, r_matrix, gamma, next_state, current_state, chosen_action):
    # Begin by finding the highest value of the next state in the q matrix
    # If Q(next_state) doesn't exist then the reward is just 0
    ns_actions = getKey(q_matrix, next_state)
    if ns_actions is None:
        ns_reward = 0
    else:
        # choose the action that yields the highest reward
        ns_max_value = 0
        for key, value in ns_actions.items():
            if value >= ns_max_value:
                ns_max_value = value
        ns_reward = ns_max_value

    # Get reward of of current state
    cs_actions = getKey(r_matrix, current_state)
    cs_reward = cs_actions[chosen_action]

    # Compute the reward for the Q matrix
    q_reward = cs_reward + gamma * ns_reward

    # Just add to the q matrix if that particular state's already in there
    for state in q_matrix.keys():
        if compareStates(state, current_state):
            q_matrix[state][chosen_action] = q_reward
            return

    # Crate a new entry if it's not already in there
    q_matrix[current_state] = {chosen_action: q_reward}


def q_learn(episodes, gamma):
    """ Q-Learning Algorithm """
    r_matrix = {}
    q_matrix = {}

    # doing 10 episodes for now 
    for i in range(episodes):
        # We know what state we're starting at, so no need to select a random one
        initial_state = CreateInitialState()
        target = initial_state.target.health

        # Add the initial state to the reward matrix
        r_matrix[initial_state] = convertState(initial_state)

        # Set the current state to start at the initial, constructed state
        current_state = initial_state

        # one episode = one depletion 
        while target > 0:
            # select a random action to take
            choices = list(getKey(r_matrix, current_state).keys())
            c_length = len(choices)
            random_index = random.randint(0, c_length - 1)  # or not - 1?

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

    # return trained learner to compute the best rotation
    return q_matrix


# returns a rotation
def traverse_q(q_matrix):
    # we know the initial state, so that's where we begin
    current_state = CreateInitialState()
    target = current_state.target.health

    chosen_actions = []

    while target > 0:
        # First find the corresponding state in the Q matrix
        for state in q_matrix.keys():
            if compareStates(current_state, state):
                actions = q_matrix[state]
                break

        # Find the action with the highest yield
        best_action = "not set"
        best_value = 0
        for key, value in actions.items():
            if value > best_value:
                best_value = value
                best_action = key

        chosen_actions.append(best_action)

        current_state = ConstructNextState(current_state, best_action)
        target = current_state.target.health

    return chosen_actions


def write_results(name, actions):
    with open(name, 'w') as file:
        for action in actions:
            file.write(action + "\n")
    print("Wrote to: " + name)


def main():
    """ Tests """
    # test_indexing()
    # test_stateTransition()
    # test_colossus()
    # test_state_comparison()
    # test_update_q()

    # Training and rotation spitting
    episodes = 25
    gamma = 0.8
    q_matrix = q_learn(episodes, gamma)
    actions = traverse_q(q_matrix)
    write_results("results_" + str(episodes) + "episodes_" +
                  str(gamma) + "gamma.txt", actions)

main()
