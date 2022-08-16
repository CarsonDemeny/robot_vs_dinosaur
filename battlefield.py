from robot import Robot
from dinosaur import Dinosaur



class Battlefield:
    def __init__(self):
        self.dinosaur = Dinosaur('Terry', 30)
        self.robot = Robot('Roomba')


    def run_battle(self):
        self.welcome_to_battle()
        self.battle()
        self.award_winner()    

    def welcome_to_battle(self):
        print('Welcome to one of the greatest battles of all time Robot Vs. Dinosaur!')

    def battle(self):
        while self.dinosaur.health > 0 and self.robot.health > 0:
            self.robot.attack(self.dinosaur) 
            self.dinosaur.attack(self.robot)
            if self.robot.health == 0 or self.dinosaur.health == 0:
                break

    def award_winner(self):
        if self.robot.health <= 0:
            print(f'The dinosaurs are back once again! {self.dinosaur.name} Wins!')
        elif self.dinosaur.health <= 0:
            print(f'After a long hard battle robots come out on top! {self.robot.name} is your winner!')                

