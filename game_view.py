import game_run
import sys
from game_setting import Player

# use these constants for the messages to make sure they are consistent
WELCOME_MESSAGE = """-------Welcome to the game-------
---Let your luck roll the dice---\n"""
GOODBYE_MESSAGE = """-----Thanks for playing the game-----"""
PROMPT_START = """Please enter 'S'\\'Q' to Start\\Quit the New Game: """
PROMPT_NAME = """What's your name: """
PROMPT_ROLL = """Please enter 'R' to Roll the Dice: """
PROMPT_PROGRESS = """------Your Current Game Progress-----\n"""
WIN_MESSAGE = """***Congratulations! You just reached the endpoint! ***"""
LOSE_MESSAGE = """------Game Lose!------"""
ASK_LOAD = """Do you want to continue playing the last unfinished game?
'Y' for yes / Others for no: """
ASK_SAVE = """Do you want to save this unfinished game?
'Y' for yes / Others for no: """

# command settings
EXIT_GAME = "Q"
START_GAME = "S"
ROLL_DICE = "R"
GAME_PROGRESS = "P"
HELP = "H"
SETTING_FILE = "trigger_setting.txt"
HELP_MESSAGE = "help_message.txt"


def check_start() -> Player:
    """
    Prompts the client for their command.
    Make sure if the client wants to start the game.
    And create the player's information.

    Returns:
        Player: class type, store the player's information
    """
    check = input(PROMPT_START)
    # code defensively
    while check not in [START_GAME, EXIT_GAME]:
        check = input(PROMPT_START)

    if check == START_GAME:
        name = input(PROMPT_NAME)
        # make sure to get an appropriate name
        while not name.isalpha():
            print("Name must be alphabetic.")
            name = input(PROMPT_NAME)
        # create player information
        player = Player(name)
        print(player)
        return player
    elif check == EXIT_GAME:
        print(GOODBYE_MESSAGE)
        sys.exit()


def print_help_message(filename: str) -> None:
    """
    Print help message of this game.
    Help message of this game is too long, so we store it in a file.

    Args:
        filename(str): the name of the file

    Returns:
        None
    """
    with open(filename, "r") as file:
        for line in file:
            if line.strip():
                print(line.strip())
    print("")


def print_trigger(trigger_type: str, value: int) -> None:
    """
    When a reward or penalty is triggered, print the prompt

    Args:
        trigger_type(str): 'hp' or 'position'
        value(int): the value of the trigger

    Returns:
        None
    """
    if trigger_type == "hp":
        if value > 0:
            print(f"You triggered a Reward! Your HP will add {value}.")
        else:
            print(f"You triggered a Penalty! Your HP will {value}.")
    elif trigger_type == "position":
        if value > 0:
            print(f"You triggered a Reward! You will move {value} more steps.")
        else:
            print(f"You triggered a Penalty! You will take {value} steps back.")


def main() -> None:
    """
    The main code to run this game.
    """
    print(WELCOME_MESSAGE)
    print_help_message(HELP_MESSAGE)

    # ask the player if he wants to continue the previous game
    check_load = input(ASK_LOAD)

    # if yes, load the game history file and create the player information
    if check_load == 'Y':
        # check if there is a game history
        if game_run.load_history():
            name, game_hp, position = game_run.load_history()
            player = Player(name, game_hp, position)
        else:
            # if something wrong with the file, start a new game
            player = check_start()
    else:
        # if no, clean game history and get ready to start a new game
        game_run.clean_history()
        player = check_start()

    # load the game's settings
    setting = game_run.load_setting(SETTING_FILE)

    # start playing the game
    command = ''
    # keeping playing unless the player input 'Q'
    while command != EXIT_GAME:
        command = input(PROMPT_ROLL)
        if command == ROLL_DICE:
            # move forward after rolling the dice
            dice = game_run.roll_dice()
            player.change_position(dice)

            # now check if a reward or penalty is triggered
            if player.position in setting:
                trigger = setting[player.position].split(" ")
                trigger_type = trigger[0]
                value = int(trigger[1])
                print_trigger(trigger_type, value)
                if trigger_type == "hp":
                    player.change_hp(value)
                elif trigger_type == "position":
                    player.change_position(value)
            else:
                print("-----Nothing Happened-----")

            # check if the player's HP drops to 0, then game over
            if game_run.check_hp(player.game_hp):
                print(LOSE_MESSAGE)
                sys.exit()
            # check if the player reached the endpoint, then game ends
            if game_run.check_endpoint(player.position):
                print(WIN_MESSAGE)
                sys.exit()

        # in case the player wants to see the status of the game
        elif command == GAME_PROGRESS:
            print(player)
        # in case the player wants to see the help message
        elif command == HELP:
            print_help_message(HELP_MESSAGE)

    # ask player whether save the unfinished game
    save_game = input(ASK_SAVE)
    if save_game == 'Y':
        game_run.save_game_history(player)
        print("Game History Saved.")
    else:
        game_run.clean_history()

    print(GOODBYE_MESSAGE)
    print(PROMPT_PROGRESS)
    print(player)
    sys.exit()


if __name__ == "__main__":
    main()
