import random
import numpy as np

def initialize_grid(n, m, initial_bed, k, incu):
    grid = np.zeros((n, m))
    row, col = initial_bed
    grid[row, col] = 2+k+incu
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
                if grid[i, j] != 1:
                    new_grid[i,j] -= 1               
                    for neighbor in get_neighbors(grid, i, j):
                        if grid[neighbor] == 0 and np.random.rand() < p:
                            new_grid[neighbor] = 1+k #set the neighbor ill                
    return new_grid

def simulate_spread_vaccines(grid, p, k, v):
    n, m = grid.shape
    uninfectedBeds = 0
    new_grid = np.copy(grid)
    for i in range(n):
        for j in range(m):
            if grid[i, j] == 0:
                uninfectedBeds += 1
            if grid[i, j] > 0:  # Check if the bed is infected or already recovered
                if grid[i, j] != 1:
                    new_grid[i,j] -= 1               
                    for neighbor in get_neighbors(grid, i, j):
                        if grid[neighbor] == 0 and np.random.rand() < p:
                            new_grid[neighbor] = 1+k #set the neighbor ill  
                            uninfectedBeds -= 1 
    
    if uninfectedBeds < v:
        v = uninfectedBeds

    vaccinated = 0
    while(vaccinated < v):
        randi = random.randint(0,n-1)
        randj = random.randint(0, m-1)
        if new_grid[randi][randj] == 0:
            new_grid[randi][randj] = -1
            vaccinated += 1

    return new_grid

def simulate_spread_bed_swap(grid, p, k, v, bs):
    n, m = grid.shape
    uninfectedBeds = 0
    new_grid = np.copy(grid)
    for i in range(n):
        for j in range(m):
            if grid[i, j] == 0:
                uninfectedBeds += 1
            if grid[i, j] > 0:  # Check if the bed is infected or already recovered
                if grid[i, j] != 1:
                    new_grid[i,j] -= 1               
                    for neighbor in get_neighbors(grid, i, j):
                        if grid[neighbor] == 0 and np.random.rand() < p:
                            new_grid[neighbor] = 1+k #set the neighbor ill  
                            uninfectedBeds -= 1 
    
    if uninfectedBeds < v:
        v = uninfectedBeds

    vaccinated = 0
    while(vaccinated < v):
        randi = random.randint(0,n-1)
        randj = random.randint(0, m-1)
        if new_grid[randi][randj] == 0:
            new_grid[randi][randj] = -1
            vaccinated += 1

    bedsSwaped = 0
    while(bedsSwaped < bs):
        randi1 = random.randint(0,n-1)
        randj1 = random.randint(0, m-1)
        randi2 = random.randint(0,n-1)
        randj2 = random.randint(0, m-1)
        tmpVal = new_grid[randi1][randj1]
        new_grid[randi1][randj1] = new_grid[randi2][randj2]
        new_grid[randi2][randj2] = tmpVal
        bedsSwaped += 1
    

    return new_grid

def simulate_spread_incubation(grid, p, k, v, bs, incu):
    n, m = grid.shape
    uninfectedBeds = 0
    new_grid = np.copy(grid)
    for i in range(n):
        for j in range(m):
            if grid[i, j] == 0:
                uninfectedBeds += 1
            if grid[i, j] > 0:  # Check if the bed is infected or already recovered
                if grid[i, j] != 1:
                    new_grid[i,j] -= 1               
                    for neighbor in get_neighbors(grid, i, j):
                        if new_grid[i,j] <= 1+k:        #check if incubation time is over
                            if grid[neighbor] == 0 and np.random.rand() < p:
                                new_grid[neighbor] = 1+k+incu #set the neighbor ill  
                                uninfectedBeds -= 1 
    
    if uninfectedBeds < v:
        v = uninfectedBeds

    vaccinated = 0
    while(vaccinated < v):
        randi = random.randint(0,n-1)
        randj = random.randint(0, m-1)
        if new_grid[randi][randj] == 0:
            new_grid[randi][randj] = -1
            vaccinated += 1

    bedsSwaped = 0
    while(bedsSwaped < bs):
        randi1 = random.randint(0,n-1)
        randj1 = random.randint(0, m-1)
        randi2 = random.randint(0,n-1)
        randj2 = random.randint(0, m-1)
        tmpVal = new_grid[randi1][randj1]
        new_grid[randi1][randj1] = new_grid[randi2][randj2]
        new_grid[randi2][randj2] = tmpVal
        bedsSwaped += 1
    

    return new_grid
