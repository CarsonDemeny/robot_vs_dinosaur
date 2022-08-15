from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('Minigun', 20)
    
    def attack(self, dinosaur):
        print(f'{self.name} attacked {dinosaur.name} with {self.active_weapon.name} and dealt {self.active_weapon.attack_power} damage!')
        dinosaur.health -= self.active_weapon.attack_power
        print(f'{dinosaur.name} has {dinosaur.health} health remaining!')
        
