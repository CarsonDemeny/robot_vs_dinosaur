from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon

dinosaur = Dinosaur('Terry', 30)
robot = Robot('Roomba')

class Battlefield:
    def __init__(self):
        self.run_battle()

    def run_battle(self):
        self.welcome_to_battle()
        self.battle()
        self.award_winner()    

    def welcome_to_battle(self):
        print('Welcome to one of the greatest battles of all time Robot Vs. Dinosaur!')

    def battle(self):
        while dinosaur.health > 0 and robot.health > 0:
            # robot.pick_weapon()
            robot.attack(dinosaur) 
            dinosaur.attack(robot)
            if robot.health == 0 or dinosaur.health == 0:
                break

    def award_winner(self):
        if robot.health <= 0:
            print(f'The dinosaurs are back once again! {dinosaur.name} Wins!')
        elif dinosaur.health <= 0:
            print(f'After a long hard battle robots come out on top! {robot.name} is your winner!')                

