import numpy as np

def initialize_grid(n, m, initial_bed):
    grid = np.zeros((n, m))
    row, col = initial_bed
    grid[row, col] = 1
    return grid

def get_neighbors(grid, row, col):
    n, m = grid.shape
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))  # Top neighbor
    if row < n - 1:
        neighbors.append((row + 1, col))  # Bottom neighbor
    if col > 0:
        neighbors.append((row, col - 1))  # Left neighbor
    if col < m - 1:
        neighbors.append((row, col + 1))  # Right neighbor
    return neighbors

def simulate_spread(grid, p, k):
    n, m = grid.shape
    new_grid = np.copy(grid)
    for i in range(n):
        for j in range(m):
            if grid[i, j] > 0:  # Check if the bed is infected or already recovered
                for neighbor in get_neighbors(grid, i, j):
                    if grid[neighbor] == 0 and np.random.rand() < p:
                        new_grid[neighbor] = k
    return new_grid

def evolve(grid, p, k, grid_list):
    new_grid = simulate_spread(grid, p, k)
    grid_list.append(new_grid.copy())
    return new_grid