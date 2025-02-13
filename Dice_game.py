from Dice_class.Dice import Dice

def main():
    print("Hello! This is an interactive dice game!")
    dice = Dice()
    dice.check_for_valid_number_of_dice()
    dice.check_for_valid_number_of_sides()

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