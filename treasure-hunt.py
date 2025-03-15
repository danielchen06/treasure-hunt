def main():
    print("Welcome to the Treasure Hunt Game!")
    max_treasures = input("Enter the maximum number of treasures each pass: ")

    while not max_treasures.isdigit() or not (1 <= int(max_treasures) <= 50):
        max_treasures = input("Enter the maximum number"
        " of treasures each pass: ")

    max_treasures = int(max_treasures)
    
    hunter1_name = input("Enter the name of the first hunter: ")
    while hunter1_name == "":
        hunter1_name = input("Enter the name of the first hunter: ")
    
    hunter2_name = input("Enter the name of the second hunter: ")
    while hunter2_name == "":
        hunter2_name = input("Enter the name of the second hunter: ")
    
    game = TreasureMap(hunter1_name, hunter2_name, max_treasures)
    game_over = False
    while not game_over:
        game_over = game.start_hunt()
        if not game_over:
            retry = input("Try again? Enter 1 for Yes or 0 for No: ")
            while retry not in ["0", "1"]:
                retry = input("Try again? Enter 1 for Yes or 0 for No: ")
            if retry == "1":
                game.generate_treasures(game.max_treasures)  
            else:
                game_over = True
    game.announce_winner()

import math
import random

class Treasure:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.value = self.calculate_value()

    def distance_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def calculate_value(self):
        distance = self.distance_from_origin()
        if distance <= 2:
            return 500
        elif distance <= 5:
            return 200
        elif distance <= 10:
            return 50
        else:
            return 0

    def __str__(self):
        return f"Treasure at ({self.x}, {self.y}) with value: {self.value}"

class Hunter:
    def __init__(self, name = "Unknown"):
        self.name = name
        self.treasures = []
    
    def collect_treasure(self, treasure):
        self.treasures.append(treasure)
        print (
            f"Hunter {self.name} collected treasure "
            f"with value: {treasure.value}"
        )
        if self.get_total_value() <= 1000:
            return False
        else:
            print(f"{self.name} has collected over 1000 points!")
            return True
    
    def get_total_value(self):
        treasure_total = 0
        for treasure in self.treasures:
            treasure_total += treasure.value
        return treasure_total
    
    def __str__(self):
        return (
            f"Hunter {self.name} has collected "
            f"treasures worth: {self.get_total_value()}"
        )

class TreasureMap:
    def __init__(self, name1="name1", name2="name2", max_treasures=10):
        self.hunter1 = Hunter(name1)
        self.hunter2 = Hunter(name2)
        self.treasures = Stack()
        self.max_treasures = max_treasures
        self.generate_treasures(max_treasures)  

    def generate_treasures(self, max_treasures):
        for treasure in range(max_treasures):
            x = random.randrange(-10, 11)  
            y = random.randrange(-10, 11) 
            new_treasure = Treasure(x, y)
            self.treasures.push(new_treasure)

    def start_hunt(self):
        round_number = 1  
        while self.treasures.size() >= 2:  
            print(f"--- Round {round_number} ---")  
            for hunter in [self.hunter1, self.hunter2]:
                if self.treasures.is_empty():
                    return False
                treasure = self.treasures.pop() 
                if hunter.collect_treasure(treasure): 
                    return True  
            round_number += 1  
        return False 

    def announce_winner(self):
        score1 = self.hunter1.get_total_value()
        score2 = self.hunter2.get_total_value()
        print("--- Final Scores ---")
        print(f"Hunter {self.hunter1.name} has "
        f"collected treasures worth: {score1}")
        print(f"Hunter {self.hunter2.name} has "
        f"collected treasures worth: {score2}")
        
        if score1 > score2:
            print(f"Congratulations! The winner is "
            f"{self.hunter1.name} with a total value of {score1}.")
        elif score2 > score1:
            print(f"Congratulations! The winner is "
            f"{self.hunter2.name} with a total value of {score2}.")
        else:
            print(f"It's a tie! Both hunters "
            f"collected treasures worth: {score1}.")