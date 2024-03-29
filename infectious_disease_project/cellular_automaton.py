import numpy as np
import random

def initialize_grid(n, m, initial_bed, k, incu):
    grid = np.zeros((n, m))
    row, col = initial_bed
    grid[row, col] = 1+k+incu
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

def simulate_spread(grid, p, k, v, bs, incu):
    n, m = grid.shape
    uninfectedBeds = 0
    new_grid = np.copy(grid)
    for i in range(n):
        for j in range(m):
            if grid[i, j] == 0:
                uninfectedBeds += 1
            if grid[i, j] > 1:  # Check if the bed is infected or already recovered
                new_grid[i,j] -= 1               
                for neighbor in get_neighbors(grid, i, j):
                    if new_grid[i,j] <= 1+k:        #check if incubation time is over
                        if grid[neighbor] == 0 and random.uniform(0, 1) < p:
                            new_grid[neighbor] = 1+k+incu #set the neighbor ill  
                            uninfectedBeds -= 1 
    
    if uninfectedBeds < v:
        v = uninfectedBeds

    if v > 0:
        new_grid = vaccinate(v, new_grid)

    if bs > 0:
        new_grid = bed_swap(bs, new_grid)
    
    return new_grid


def vaccinate(v, new_grid):
    n, m = new_grid.shape
    vaccinated = 0
    while(vaccinated < v):
        randi = random.randint(0,n-1)
        randj = random.randint(0, m-1)
        if new_grid[randi, randj] == 0:
            new_grid[randi, randj] = -1
            vaccinated += 1

    return new_grid

def bed_swap(bs, new_grid):
    n, m = new_grid.shape
    bedsSwaped = 0
    while(bedsSwaped < bs):
        randi1 = random.randint(0,n-1)
        randj1 = random.randint(0, m-1)
        randi2 = random.randint(0,n-1)
        randj2 = random.randint(0, m-1)
        tmpVal = new_grid[randi1, randj1]
        new_grid[randi1, randj1] = new_grid[randi2, randj2]
        new_grid[randi2, randj2] = tmpVal
        bedsSwaped += 1

    return new_grid