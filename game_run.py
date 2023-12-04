import random
from game_setting import Player


# game parameters settings
END_POINT = 30
GAME_HISTORY = "game_history.txt"


def roll_dice() -> int:
    """
    Roll the dice and get a random integer between 1 and 6.

    Return:
        int: the value of the dice
    """
    dice = random.randint(1, 6)
    print(f"It's a {dice} and you will move {dice} steps forward!")
    return dice


def load_setting(filename: str) -> dict:
    """
    Load the game's reward and punishment settings.

    Example:
        >>> load_setting("test_setting.txt")
        {3: 'hp -10', 5: 'position -5'}

    Args:
        filename(str): the name of the file

    Returns:
        dict: store the information in a dictionary
    """
    setting = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                if line.strip():
                    trigger = line.strip().split(",")
                    setting[int(trigger[0])] = trigger[1]
        return setting
    except FileNotFoundError:
        print("Setting file is missing!")
    except PermissionError:
        print("You don't get the permission of the setting file.")
    except IOError:
        print("Error!")


def check_endpoint(position: int) -> bool:
    """
    check if the player has reached the endpoint.

    Example:
        >>> check_endpoint(10)
        False
        >>> check_endpoint(31)
        True

    Args:
        position(int): the player's current position

    Returns:
        bool: if the player has reached the endpoint
    """
    if position < END_POINT:
        return False
    else:
        return True


def check_hp(hp: int) -> bool:
    """
    check the player's HP value to see if the game is over.

    Example:
        >>> check_hp(0)
        True
        >>> check_hp(20)
        False

    Args:
        hp(int): the player's HP value

    Returns:
        bool: wheither the game is over
    """
    if hp <= 0:
        return True
    else:
        return False


def load_history(filename=GAME_HISTORY) -> tuple:
    """
    Load the game history and get the latest game's information.

    Example:
        >>> load_history("test_history_1.txt")
        Something Wrong with the game history. Please Start a New Game
        ()
        >>> load_history("test_history_2.txt")
        ('jack', 50, 10)

    Args:
        filename(str): name of the file, default to be GAME_HISTORY
    Returns:
        tuple: the latest game's information
    """
    setting = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.strip():
                    setting.append(line.strip())
        if len(setting) != 3:
            print("Something Wrong with the game history. Please Start a New Game")
            return ()
        else:
            name = setting[0]
            game_hp = int(setting[1])
            position = int(setting[2])
            return name, game_hp, position
    except FileNotFoundError:
        print("Game History is missing! Please Start a New Game")
    except PermissionError:
        print("You don't get the permission of the setting file.")
    except IOError:
        print("Error!")


def clean_history(filename=GAME_HISTORY) -> None:
    """
    Clean the old game history.

    Args:
        filename(str): name of the file, default to be GAME_HISTORY
    Returns:
        None
    """
    try:
        with open(filename, 'w') as file:
            file.truncate(0)
    except FileNotFoundError:
        print("Game History is missing!")
    except PermissionError:
        print("You don't get the permission of the setting file.")
    except IOError:
        print("Error!")


def save_game_history(player: Player) -> None:
    """
    Save this game history.

    Args:
        player(Player): player information
    Returns:
        None
    """
    try:
        with open(GAME_HISTORY, 'w') as file:
            file.write(player.name + '\n')
            file.write(str(player.game_hp) + '\n')
            file.write(str(player.position))
    except FileNotFoundError:
        print("Game History is missing!")
    except PermissionError:
        print("You don't get the permission of the setting file.")
    except IOError:
        print("Error!")
