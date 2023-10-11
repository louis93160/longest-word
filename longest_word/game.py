import random
import string

size = 9

class Game:
    def __init__(self) -> list:

        self.grid = random.choices(string.ascii_uppercase + string.digits, k=size)
        pass

    def is_valid(self, word:str) -> bool:

        if len(self.grid) == 9:
            return True
        else:
            return False


game = Game()
#print(game.grid)
my_word = "BAROQUE"
game.is_valid(my_word)

""" if __name__ == "__main__":
    print(Game) """
