from grid import Grid
from game import Game

if __name__ == '__main__':
    grid = Grid(6, 7)
    game = Game(grid, 4, 2)
    game.play()