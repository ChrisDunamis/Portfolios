from Dice_Art import dice_roll
from random import randint
from sys import exit


MY_COURSE = "Project - Dice Roller Program"
MY_SUBJECT = "DICE ROLLER"

print("""
Course:     %s
Subject:    %s
""" % (MY_COURSE, MY_SUBJECT))

dice_value = []  # An empty list variable to contain the values of dice rolls.
dice_total = 0   # Variable set to '0' to get the sum of dice rolls; i.e. if 3 dices are being rolled sum = value1 +
# value 2 + value 3.

try:
    roll_dice = int(input("How many times do you want to roll the dice?   "))

except ValueError as value_error:
    print(('-' * 100) + "\n" +
          "Riddle: I am a square and I have six sides, what am I...?" + "\n\t\t" +
          "You will need to restart the program and try again." + "\n\n" +

          "Error -", str(value_error).capitalize(), "<--=-- input." + "\n\t\t" +
          "I need to be a number (not a fraction or decimal)..." + "\n\t\t" +
          "Dice roll failure, due to value error." + "\n" +
          ('-' * 100))
    exit(1)
except KeyboardInterrupt:
    print("\n" + ('-' * 100) + "\n" +
          "System Interrupted: End of program." + "\n" +
          "If you wish to try again, please restart the program..." + "\n" +
          ('-' * 100))
    exit(2)

# ------------------------------------------------- Display Method 1 --------------------------------------------------#


def display_dice1():
    for each_dice_roll in range(roll_dice):     # This For Loop iterates through the "Variable: roll_dice", from this,
        dice_value.append(randint(1, 6))  # we can iterate the value(s) within the For Loop "Variable/Index:
        # each_dice_roll". In the "Variable: dice_value", we can append the result(s) from the iterated value(s), using
        # the "Module Class: randint".
    for dice_display in range(roll_dice):  # The For Loop here is made for displaying the Dice Art ASCII from the
        # "File/Module: Dice_Art.py". In this For Loop, we display the number of dice roll(s) from each dice rolled.
        print("\n" + "|Dice: {value}|".center(20, ' ').format(value=(dice_display + 1)))

        for dice_display_index in dice_roll.get(dice_value[dice_display]):  # In this For Loop, we use the "Dictionary
            print(dice_display_index)  # Method: get()", to iterate through the values from the "Variable: dice_roll",
            # from the "File/Module: Dice_art.py". The argument provided is the given value(s) from the "Variable:
            # dice_value" at the index of the For Loop "Variable: dice_display".

    print(end='')
# -------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------- Display Method 2 ------------------------------------------------- #


def display_dice2():
    print()

    for each_dice_roll in range(roll_dice):  # This For Loop iterates through the "Variable: roll_dice", from this, we
        dice_value.append(randint(1, 6))     # can iterate the value(s) within the For Loop "Variable/Index:
        # each_dice_roll". In the "Variable: dice_value", we can append the result(s) from the iterated value(s), using
        # the "Module Class: randint".
        print("|Dice: {value}|".center(19, ' ').format(value=(each_dice_roll + 1)), end=' ')

    print()

    for dice_display in range(5):
        for dice_display_index in dice_value:
            print(dice_roll.get(dice_display_index)[dice_display], end=' ')

        print()
# -------------------------------------------------------------------------------------------------------------------- #


try:
    select_display = int(input("Select Display [1/2]:   "))

    if select_display == 1:
        display_dice1()
    elif select_display == 2:
        display_dice2()
    else:
        print(('-' * 100) + "\n" +
              "Please select a valid display option:" + "\n" +
              "     - 1 (Display Option 1: Vertically)" + "\n" +
              "     - 2 (Display Option 2: Horizontally)")
except ValueError as value_error:
    print(('-' * 100) + "\n" +
          "Error -", str(value_error).capitalize(), "<---- input.\n\t\t" +
          "Please enter a valid display option." + "\n" +
          ('-' * 100))
    exit(1)
except KeyboardInterrupt:
    print("\n" + ('-' * 100) + "\n" +
          "System Interrupted: End of program." + "\n" +
          "If you wish to try again, please restart the program..." + "\n" +
          ('-' * 100))
    exit(2)
except NameError as name_error:
    print(('-' * 100) + "\n" +
          "Error -", str(name_error).capitalize() + ", due to an error from the last input." + "\n" +
          ('-' * 100))
    exit(3)

for dice_sum in dice_value:  # This For Loop calculates the Sum of the total dice rolled. From the value(s) in the
    dice_total += dice_sum   # "Variable: dice_value", we iterate through the For Loop "Variable/Index: dice_sum". The
    # "Variable: dice_total" stores the values from the iterated value(s).

print("\n" + "Total Dice Roll(s):", str(dice_total))
# -------------------------------------------------------------------------------------------------------------------- #
