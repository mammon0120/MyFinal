import random


# game parameters settings
END_POINT = 30


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
        bool: if the game is over
    """
    if hp <= 0:
        return True
    else:
        return False
