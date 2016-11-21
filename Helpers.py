""" Juan Bautista Berretta and Jack Reynolds """

from Classes import *

""" Creates the initial state, in which all the abilities are available for use. """
def CreateInitialState():
    abilities = []
    target = Target(100)

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
    hamstring = Ability("hamstring", 5543, "hamstring", None, 8)

    """ Special abilities. """
    battle_cry = Ability("battle_cry", None, "battle_cry", 60, None)

    abilities = [mortal_strike, slam, whirlwind, colossus_smash,
                    rend, bladestorm, execute, cleave, hamstring, battle_cry]

    state = State(abilities, target)

    return state
