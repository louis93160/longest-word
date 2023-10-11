from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
        new_game = Game()

        grid = new_game.grid

        assert type(grid) == list
        assert len(grid) == 9
        for letter in grid:
            assert letter in string.ascii_uppercase
