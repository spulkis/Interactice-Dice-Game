import random
from collections import deque

class Dice:
    def __init__(self, number_of_dice, number_of_sides):
        self.number_of_dice = number_of_dice
        self.number_of_sides = number_of_sides
        self.individual_rolls = None
        self.previous_rolls = deque(maxlen=100)

    @classmethod # This mean I can call this method without instantiating a Dice first
    def get_information(cls): # Request input values inside of a class
        while True:
            try:
                number_of_dice = int(input("How many dice do you want to play with? "))
                if 1 <= number_of_dice <= 5:
                    number_of_sides = int(input("How many sides does your dice have? "))
                    if  1 <= number_of_sides <= 100:
                        return cls(number_of_dice, number_of_sides)
                    else:
                        raise ValueError ("Invalid number of sides. Please enter a value between 1 and 100.")
                else:
                    raise ValueError ("Invalid number of dice. Please enter a value between 1 and 5.")
            except ValueError as error:
                print(error)
       
    def __str__(self):
        return f"You rolled {', '.join(str(x) for x in self.individual_rolls)} (You are playing with {self.number_of_dice} dice which have {self.number_of_sides} sides)"
    
    def roll(self):
        self.individual_rolls = [random.choice(range(1, self.number_of_sides + 1)) for _ in range(self.number_of_dice)]
        self.previous_rolls.append(self.individual_rolls)
        return self.individual_rolls
    
    def history_of_previous_rolls(self):
        if self.previous_rolls:
            output = "\nRolls history:\n"
            for index, roll in enumerate(self.previous_rolls):
                output += f"{index+1}. {roll}\n"
            return output
        else:
            return "No previous rolls yet."

def main():
    print("Hello! This is an interactive dice game!")
    dice = Dice.get_information()

    while True:
        dice.roll()
        print(dice.history_of_previous_rolls())
        print(dice)
        # Ask user if they want to roll again
        repeat_roll = input("Do you want to roll again? (y/n): ")
        if repeat_roll.lower() != 'y':
            print("Bye!")
            break

if __name__ == "__main__":
    main()