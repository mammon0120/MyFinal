class Player:
    """
    Creates the player's role information.
    Attributes: name, game_hp, position
    Methods:change_hp, change_position
    """
    def __init__(self, name: str, game_hp=100, position=0):
        self.__name = name
        self.game_hp = game_hp
        self.position = position

    @property
    def name(self):
        return self.__name

    def change_hp(self, hp_value: int):
        self.game_hp += hp_value
        if self.game_hp >= 100:
            self.game_hp = 100
        return self.game_hp

    def change_position(self, position_value: int):
        self.position += position_value
        return self.position

    def __str__(self):
        output = (f"***Player Information***\n"
                  f"Name: {self.name:>13}\nGAME_HP: {self.game_hp:>10}\nPOSITION_NOW: {self.position:>5}")
        return output
