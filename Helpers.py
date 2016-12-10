""" Juan Bautista Berretta and Jack Reynolds """

GCD = 1.5

from classes import *
import copy


""" Creates the initial state, in which all the abilities are available for use. """
def CreateInitialState():
    abilities = []
    target = Target(1000000)

    """ name - damage - effects - cool down - cost """

    """ Without effects. """
    mortal_strike = Ability("mortal_strike", 17263, None, 5, 16)
    slam = Ability("slam", 11938, None, 0, 16)

    """ With effects. """
    colossus_smash = Ability("colossus_smash", 14166, "colossus_smash", 30, 0)
    execute = Ability("execute", 8552, "execute", 0, 8)

    """ Special abilities. """
    battle_cry = Ability("battle_cry", None, "battle_cry", 60, None)
    avatar = Ability("avatar", 0, "avatar", 90, 0) 


    abilities.extend([mortal_strike, slam, colossus_smash,
                      execute, avatar, battle_cry])

    state = State(abilities, target)

    return state

""" Constructs and returns the next state depending on the ability chosen. """
def ConstructNextState(current_state, ability_used):
    # 1) Start ability cooldown (CD - GCD), and decrease pertinent rage 
    # 2) Iterate through rest of abilities and decrease their CDs as well
    # 3) Check rage generation

    # Constructing new state out of old. All changes will be done to the new state object.
    new_state = State(copy.deepcopy(current_state.abilities), copy.deepcopy(current_state.target))
    new_state.target.checkEffects()
    
    # Decreasing all ability CDs by GCD
    for ability in new_state.abilities:
        ability.remaining_time -= GCD
        if ability.name == ability_used:
            # Updating rage
            new_state.rage -= ability.cost
            new_state.target.takeDamage(ability) # damages and applies effects to target

    # Auto attack timer for rage regeneration
    new_state.decreaseTimer(GCD, new_state.target)

    new_state.target.printStatus()
    return new_state

# Converts a state into a matrix entry
def convertState(state):
    row = {}
    for ability in state.abilities:
        if ability.canUse():
            # the following abilities are affect damage for future states and should be considered:
            # colossus smash, avatar, battle cry
            # but.. Avatar and CS don't work within the global cooldown
            damage = ability.damage
            if state.target.colossus_smash > 0:
                damage = damage + ((damage/100) * 47) # + 47% damage boost
            if state.target.battle_cry > 0:
                damage = damage * 2
            if state.target.avatar > 0:
                damage = damage + ((damage/100) * 20) # + 20% damage boost
            row[ability.name] = damage
    return row
        # we don't even include the abilities that can't be used in the dictionary

# Used to compare states to see if they're equal
def compareStates(state_1, state_2):
    s1_abilities = convertState(state_1)
    s2_abilities = convertState(state_2)

    for key, value in s1_abilities.items():
        if key not in list(s2_abilities.keys()):
            return False

    s1_target = (state_1.target.health / state_1.target.full_health) * 100
    s2_target = (state_2.target.health / state_2.target.full_health) * 100
    print(s1_target)
    print(s2_target)

    # target health is discretized as 10% intervals 
    difference = s1_target - s2_target
    if abs(difference) >= 10:
        return False

    return True

# Gets the corresponding key for the dictionary in {state : {}}
def getKey(dict, s1):
    for s2 in list(dict.keys()):
        if compareStates(s1, s2):
            return dict[s2]
        
