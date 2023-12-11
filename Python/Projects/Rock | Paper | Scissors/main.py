from random import choice
from sys import exit


MY_COURSE = "Project - Rock | Paper | Scissors"
MY_SUBJECT = "RPS GAME"

print("""
Course:     %s
Subject:    %s

-------------------------| Rock | Paper | Scissors |-------------------------""" % (MY_COURSE, MY_SUBJECT))

QUIT_COMMANDS = ("Q", "Quit")  # Input commands for quitting the session.
RPS_CHOICES = ("Rock", "Paper", "Scissors")  # Game Choices...

player_selection = None  # Set to "None", for the "While Loop" interval.

"""The "While Loop" is set to "True" if the player selection is in the "Constant Variables: RPS_CHOICES and 
QUIT_COMMANDS", otherwise, the preceding variables will take effect."""
while (player_selection not in RPS_CHOICES) or (player_selection not in QUIT_COMMANDS):
    comp_selection = choice(RPS_CHOICES)  # Selection from the "Module: random".
    player_selection = input(""""Choice Input:
    - Rock
    - Paper
    - Scissors
(Or you can input ['q' | "quit"] to end the program)
    
Enter a choice::   """).title()

    if player_selection in QUIT_COMMANDS:  # While in game mode, you can exit the game. Set as Exit Status (1).
        exit("\n" + "Session Ended (1)" + "\n" +
             " © RPS GAME ".center(77, '-'))

    if player_selection == "":  # Detects an empty string/input.
        print("""
Please choose from the lists below:
    - Rock
    - Paper
    - Scissors
""")
    elif player_selection not in RPS_CHOICES:
        print(('-' * 77) +
              """
Input "%s" is not in the list of choice, please choose from the lists below:
    - Rock
    - Paper
    - Scissors
""" % player_selection)
    elif player_selection == comp_selection:  # Win Case Scenario...
        print("\n" + "Player:   %s" % player_selection + "\n" +
              "Computer: %s" % comp_selection + "\n\n" +

              "It's a tie!" + "\n" +
              '-' * 77)
    elif (player_selection == "Rock") and (comp_selection == "Scissors"):  # Win Case Scenario...
        print("\n" + "Player:   %s" % player_selection + "\n" +
              "Computer: %s" % comp_selection + "\n\n" +

              "You Win!" + "\n" +
              '-' * 77)
    elif (player_selection == "Paper") and (comp_selection == "Rock"):  # Win Case Scenario...
        print("\n" + "Player:   %s" % player_selection + "\n" +
              "Computer: %s" % comp_selection + "\n\n" +

              "You Win!" + "\n" +
              '-' * 77)
    elif (player_selection == "Scissors") and (comp_selection == "Paper"):  # Win Case Scenario...
        print("\n" + "Player:   %s" % player_selection + "\n" +
              "Computer: %s" % comp_selection + "\n\n" +

              "You Win!" + "\n" +
              '-' * 77)
    else:  # Loose Case Scenario...
        print("\n" + "Player:   %s" % player_selection + "\n" +
              "Computer: %s" % comp_selection + "\n\n" +

              "You Loose!" + "\n" +
              '-' * 77)

    # While in game mode, the user can choose to continue. Set as Exit Status (2), if user declines the game.
    if input("Would you like to try again [y/n or yes/no]:     ").title() not in ("Y", "Yes"):
        exit(('-' * 77) + "\n" +
             "End of Program (1)" + "\n" +
             " © RPS GAME ".center(77, '-'))
    else:
        print('-' * 77)
