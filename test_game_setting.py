from game_setting import Player
import unittest


class SettingTest(unittest.TestCase):
    """
    Test if the program can correctly create the player's information.
    """
    def test_init(self):
        player = Player('May')
        self.assertEqual(player.name, 'May')
        self.assertEqual(player.game_hp, 100)
        self.assertEqual(player.position, 0)

    def test_change_hp(self):
        player = Player('May', 50, 10)
        player.change_hp(-20)
        self.assertEqual(player.game_hp, 30)

        player.change_hp(10)
        self.assertEqual(player.game_hp, 40)

    def test_change_position(self):
        player = Player('May', 50, 10)
        player.change_position(-5)
        self.assertEqual(player.position, 5)

        player.change_position(6)
        self.assertEqual(player.position, 11)


def main():
    unittest.main(verbosity=3)
