import random
from collections import deque

class Dice:
    def __init__(self, number_of_dice=None, number_of_sides=None):
        """Initializes the Dice object with the number of dice and sides."""
        self.number_of_dice = number_of_dice
        self.number_of_sides = number_of_sides
        self.individual_rolls = None
        self.previous_rolls = deque(maxlen=100)

    def check_for_valid_number_of_dice(self):
        """Prompts the user for the number of dice and validates the input. Ensures the input is an integer between 1 and 5 (inclusive)."""
        while True:
            try:
                self.number_of_dice = int(input("How many dice do you want to play with? "))
                if 1 <= self.number_of_dice <= 5:
                    return self.number_of_dice
                else:
                    raise ValueError
            except ValueError:
                print("Invalid number of dice. Please enter a value between 1 and 5.")

    def check_for_valid_number_of_sides(self):
        """Prompts the user for the number of sides and validates the input. Ensures the input is an integer between 1 and 100 (inclusive)."""
        while True:
            try:
                self.number_of_sides = int(input("How many sides does your dice have? " ))
                if 1 <= self.number_of_sides <= 100:
                    return self.number_of_sides
                else:
                    raise ValueError
            except ValueError:
                print("Invalid number of sides. Please enter a value between 1 and 100.")
       
    def __str__(self):
        """Returns a string representation of the Dice object, displaying the total displaying the rolls."""
        return f"You rolled {', '.join(str(x) for x in self.individual_rolls)} (You are playing with {self.number_of_dice} dice which have {self.number_of_sides} sides)"
    
    def roll(self):
        """
        Rolls the dice and stores the results

        - Generates a list of random integers using the `random` module, representing the individual roll results for each die.
        - Appends the current roll to the history of previous rolls (up to 100).
        """
        self.individual_rolls = [random.choice(range(1, self.number_of_sides + 1)) for _ in range(self.number_of_dice)]
        self.previous_rolls.append(self.individual_rolls)
        return self.individual_rolls
    
    def history_of_previous_rolls(self):
        """Returns a formatted string representing the history of previous rolls."""
        if self.previous_rolls:
            output = "\nRolls history:\n"
            for index, roll in enumerate(self.previous_rolls):
                output += f"{index+1}. {roll}\n"
            return output
        else:
            return "No previous rolls yet."