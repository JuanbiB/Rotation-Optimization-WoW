import random

"""Juan Bautista Berretta & Jack Reynolds 2016
    Reinforcement Learning Project """

            
""" Ability class to encapsulate the the functionality of
    different abilities. """
class Ability:
    def __init__(self, name, damage, effects, cd, cost):
        self.name = name
        self.damage = damage
        self.effects = effects
        self.cost = cost
        self.cd = cd
        self.remaining_time = 0

    """ To check if an ability is on CD or not. """
    def canUse(self):
        if self.remaining_time <= 0:
            return True
        else:
            return False

    """ Returns raw damage and activates CD. """
    def useAbility(self):
        crit_chance = random.randfloat(1, 100)

        self.remaining_time = self.cd

        if crit_chance < 15.07:
            return self.damage * self.damage
        else:
            return self.damage


""" Target objects that gets passed from state to state, in order
    be able to finish an episode (when the health's depleted). """
class Target:
    def __init__(self, health):
        self.health = health
        self.effects = {} # {effect : duration}
        self.damage_boost = 0.0

    def takeDamage(self, ability):
        self.health -= ability.useAbility()

        # UNDER DEVELOPMENT, ABILITIES WITH EFFECTS
        name = ability.effects
        if name == "rend": # dot
            self.effects["rend"] = 15
        elif name == "colossus_smash": # damage increase
            self.damage_boost = .47
        elif name == "bladestorm": # channel
            return
        elif name == "execute": # additional damage
            return
        elif name == "cleave": # additional damage to ww
            return
        else: # battlecry, increased CS
            return
        
    
""" State class that holds a list of abilities and the state of the current target. """
class State:
    def __init__(self, abilities, target):
        self.abilities = abilities
        self.target = target
        self.rage = 100

    def decreaseRage(self, amount):
        self.rage -= amount


