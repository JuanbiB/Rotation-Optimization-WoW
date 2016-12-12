import random

"""Juan Bautista Berretta & Jack Reynolds 2016
    Reinforcement Learning Project """
GCD = 1.5
            
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

    """ Returns damage and activates CD. """
    def useAbility(self, battle_cry):
        crit_chance = random.uniform(0.0, 100.0)
        self.remaining_time = self.cd

        # battlecry guarantees crit strike
        if not battle_cry:
            if crit_chance < 15.07:
                print("Critical strike for ability: " + self.name)
                return self.damage * 2
            else:
                return self.damage
        else:
                return self.damage * 2


""" Target objects that gets passed from state to state, in order
    be able to finish an episode (when the health's depleted). """
class Target:
    def __init__(self, health):
        self.health = health
        self.full_health = health
        self.colossus_smash = 0 # duration left in damage boost
        self.battle_cry = 0  # guaratneed crit strike
        self.avatar = 0

    def takeDamage(self, ability):
        if self.battle_cry:
            damage = ability.useAbility(True) # Parameter guarantees critical strikes
        else:
            damage = ability.useAbility(False)

        # original damage kept for boosting abilities
        og_damage = damage

        # damage modifying
        if self.colossus_smash > 0:
            damage += ((og_damage/100) * 47) # + 47% damage boost
        if self.avatar > 0:
            damage += ((og_damage/100) * 20) # + 20% damage boost
            
        # CD refreshing
        elif ability.name == "colossus_smash":
            self.colossus_smash = 8
        elif ability.name == "avatar":
            self.avatar = 20
        elif ability.name == "battle_cry":
            self.battle_cry = 5

        # Actual health deduction
        self.health -= damage

    # Used to decrease timers of enhancing effects
    def checkEffects(self):
        self.avatar -= GCD
        self.colossus_smash -= GCD
        self.battle_cry -= GCD

    # Useful for debugging
    def printStatus(self):
        print("\nTarget status: ")
        print("Life: " + str((self.health / self.full_health) * 100))
        print("Cooldowns:")
        print("\tColossus Smash: " + str(self.colossus_smash))
        print("\tBattle Cry: " + str(self.battle_cry))
        print("\tAvatar: " + str(self.avatar) + "\n")
        print("<------------------------>")
        
    
""" State class that holds a list of abilities and the state of the current target. """
class State:
    def __init__(self, abilities, target):
        self.abilities = abilities
        self.target = target
        self.rage = 100
        self.auto_attack_timer = 3.6

    def decreaseRage(self, amount):
        self.rage -= amount

    def decreaseTimer(self, amount, target):
        self.auto_attack_timer -= amount

        if self.auto_attack_timer <= 0:
            target.rage += 25 # increase rage
            self.auto_attack_timer += 3.6 # reset timer
