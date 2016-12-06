""" Juan Bautista Berretta and Jack Reynolds """

GCD = 1.5

from Classes import *

""" Creates the initial state, in which all the abilities are available for use. """
def CreateInitialState():
    abilities = []
    target = Target(10000)

    """ name - damage - effects - cool down - cost """

    """ Without effects. """
    mortal_strike = Ability("mortal_strike", 17263, None, 5, 16)
    slam = Ability("slam", 11938, None, None, 16)
    whirlwind = Ability("whirlwind", 9661, None, None, 20)

    """ With effects. """
    colossus_smash = Ability("colossus_smash", 14166, "colossus_smash", 30, None)
    rend = Ability("rend", 22755, "rend", None, 12)
    bladestorm = Ability("bladestorm", 87029, "bladestorm", 90, None)
    execute = Ability("execute", 8552, "execute", None, 8)
    cleave = Ability("cleave", 4751, "cleave", 5.62, 8)

    """ Special abilities. """
    battle_cry = Ability("battle_cry", None, "battle_cry", 60, None)

    abilities.extend([mortal_strike, slam, whirlwind, colossus_smash,
                      rend, bladestorm, execute, cleave, battle_cry])

    state = State(abilities, target)

    return state

""" Constructs and returns the next state depending on the ability chosen. """
def ConstructNextState(current_state, ability_used):
    # 1) Start ability cooldown (CD - GCD), and decrease pertinent rage 
    # 2) Iterate through rest of abilities and decrease their CDs as well
    # 3) Check rage generation

    # Constructing new state out of old. All changes will be done to the new state object.
    new_state = State(current_state.abilities, current_state.target)

    # Decreasing all ability CDs by GCD
    for ability in new_state.abilities:
        ability.remaining_time -= GCD
        if ability.name == ability_used:
            # Updating rage. 
            new_state.rage -= ability.cost
            new_state.target.takeDamage(ability) # damages and applies effects to target

    # Auto attack timer for rage regeneration
    new_state.decreaseTimer(GCD, new_state.target)
    # Checking our only DoT 
    new_state.target.checkRend()

    return new_state

# Converts a state into a matrix entry
def convertState(state):
    row = {}
    for ability in state.abilities:
        if ability.canUse():
            row[ability.name] = ability.damage
    return row

        # we don't even include the abilities that can't be used in the dictionary
    
    

