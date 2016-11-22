import random

"""Juan Bautista Berretta & Jack Reynolds 2016
    Reinforcement Learning Project """

""" DoT = Damage over Time
    Used to keep track of all of such abilities that a target is
    afflicted by. """
class Dot:
    def __init__(self, damage, interval):
        self.damage = damage
        self.interval = interval

    def tick(self, target):
        target.health -= self.damage

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

    """ Tentative? Are we going to do things in real time?? """
    def canUse(self):
        if self.remaining_time <= 0:
            return True
        else:
            return False

    """ Just basic calculation of raw damage, does not apply special effects. """
    def calculateDamage(self):
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
        self.dots = []

    def takeDamage(self, ability):
        self.health -= ability.calculateDamage()


""" State class that holds a list of abilities and the state of the current target. """
class State:
    def __init__(self, abilities, target):
        self.abilities = abilities
        self.target = target
        self.rage = 100

    def decreaseRage(self, amount):
        self.rage -= amount


