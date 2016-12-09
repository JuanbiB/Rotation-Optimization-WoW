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

        # battlecry guaratness crit strike
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
        self.colossus_smash = 0.0 # duration left in damage boost
        self.rend = 0.0 # duration remaining on rend
        self.bladestorm = 0.0 # duration left in channel
        self.cleave = 0.0 # duration for %20 damage boost
        self.battle_cry = 0.0  # guaratneed crit strike
        self.whirlwind_boost = 0 # 20% damage boost to ability

    def takeDamage(self, ability):
        if self.battle_cry:
            damage = ability.useAbility(True) # Parameter guarantees critical strikes
        else:
            damage = ability.useAbility(False)

        og_damage = damage

        # damage modifying
        if self.colossus_smash > 0:
            damage = damage + ((damage/100) * 47) # + 47% damage boost
        if ability.name == "whirlwind" and self.whirlwind_boost > 0:
            damage = damage + ((og_damage/100) * 20) # %20 damage increase from original damage on whirlwind
            self.whirlwind -= 1
            
        # CD refreshing
        elif ability.name == "colossus_smash":
            self.colossus_smash = 8
        elif ability.name == "cleave":
            self.whirlwind_boost += 1
        elif ability.name == "rend": # refresh CD for rend
            self.rend = 15
        elif ability.name == "bladestorm": # refresh CD for BS 
            self.bladestorm = 5.6

        if damage != 0:
            print("Applied " + ability.name + " for: " + str(damage) + "\n\t " + str(self.health) + " --> " + str(self.health - damage))
        self.health -= damage

    # Used to check our only DoT, rend
    def checkRend(self):
        # Every tick has a chance to crit! (not going to include the 100% boost from battle cry)
        if self.rend > 0:
            base = 2275.5
            crit_chance = random.uniform(0.0, 100.0)
            if crit_chance <= 15.07:
                rend_dmg = base * 2
            else:
                rend_dmg = base
                
            print("Applied rend tick for " + str(rend_dmg) + "\n\t " + str(self.health) + " --> " + str(self.health - rend_dmg))
            self.health -= rend_dmg
            self.rend -= GCD
    
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
