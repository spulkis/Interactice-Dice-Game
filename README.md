[![python](https://img.shields.io/badge/Python-gray?logo=Python)](https://www.python.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
## Interactive Dice Game

This is a fun and simple Python program that simulates an interactive dice game. You can specify the number of dice (between 1 and 5) and the number of sides on each die (between 1 and 100). The program will then allow you to roll the dice and see the individual results, as well as keep track of your previous rolls.

### How to Play

1. Clone or download the repository.
2. Run the program using `python Dice_game.py` (or the appropriate command for your system).
3. Follow the prompts to specify the number of dice and sides.
4. The program will display the results of your roll and ask if you want to roll again.
5. You can keep rolling the dice as many times as you like.

### Example Usage

```
Hello! This is an interactive dice game!
How many dice do you want to play with? 2
How many sides does your dice have? 6
You rolled 3, 4 (You are playing with 2 dice which have 6 sides)

Rolls history:
1. [3, 4]

Do you want to roll again? (y/n): y
You rolled 2, 1 (You are playing with 2 dice which have 6 sides)

Rolls history:
1. [3, 4]
2. [2, 1]

Do you want to roll again? (y/n): n
Bye!
```

### Features

- Roll between 1 and 5 dice.
- Specify the number of sides on each die (between 1 and 100).
- See the individual results of each roll.
- Keep track of your previous rolls (up to the last 100).

### Suggestions for future improvements

- **Dynamic Dice Selection:** Currently, the program requires specifying the number of dice and sides at the beginning. In the future, allowing users to change the number of dice and/or the number of sides between rolls would enhance flexibility.
- **Multi-sided Dice Support:** The current implementation assumes all dice have the same number of sides. Extending the program to handle dice with different side counts (e.g., a standard six-sided die and a four-sided die) would broaden its functionality.
- **Weighted Dice:** Adding support for weighted dice, where each side has a different probability of rolling, would introduce an exciting element of customization.
- **Scoring System:** The game can be extended to include a scoring system, which would add a layer of complexity and engagement. A scoring system would make the game more goal-oriented and allow players to track their progress over time.

### Dependencies

Python 3 (https://www.python.org/downloads/)

**Feel free to fork this repository and make your own modifications!**