import numpy as np

def game_of_life(grid):
    neighbors = sum(np.roll(np.roll(grid, i, 0), j, 1) for i in (-1, 0, 1) for j in (-1, 0, 1) if (i, j) != (0, 0))
    return (neighbors == 3) | (grid & (neighbors == 2))

grid = np.random.randint(2, size=(5, 5))
for _ in range(5):  # Run for 5 generations
    grid = game_of_life(grid)
    print(grid)
