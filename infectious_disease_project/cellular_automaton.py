import random
import numpy as np


class CellularAutomaton:
    def __init__(self, n, m, initial_bed, p, k):
        self.n = n
        self.m = m
        self.p = p
        self.k = k
        self.grid = self.initialize_grid(initial_bed)

    def initialize_grid(self, initial_bed):
        # Implement code to initialize the grid based on the provided initial_bed
        # Set the infected bed and its neighboring beds accordingly
        # Return the initialized grid

        # Create an empty grid of size n x m
        grid = [['healthy'] * self.m for _ in range(self.n)]

        # Set the initial infected bed
        initial_bed = initial_bed.split(',')
        row, col = int(initial_bed[0]), int(initial_bed[1])
        grid[row][col] = 'ill'

        # Set the neighboring beds as infectables
        neighbors = self.get_neighbors(row, col)
        for neighbor in neighbors:
            n_row, n_col = neighbor
            grid[n_row][n_col] = 'infectable'

        return grid

    def simulate_spread(self):
        # Iterate over the grid for k days or until no more changes occur
        for day in range(self.k):
            changes_occurred = False

            # Create a copy of the current grid for comparison
            prev_grid = [row[:] for row in self.grid]

            # Iterate over each cell in the grid
            for row in range(self.n):
                for col in range(self.m):
                    # Skip cells that are already immune or healthy
                    if self.grid[row][col] in ['healthy', 'immune']:
                        continue

                    # Check the neighbors of the current cell
                    neighbors = self.get_neighbors(row, col)
                    for neighbor_row, neighbor_col in neighbors:
                        # Spread the disease to infectable neighbors with a probability p
                        if prev_grid[neighbor_row][neighbor_col] == 'infectable':
                            if random.random() < self.p:
                                self.grid[neighbor_row][neighbor_col] = 'ill'
                                changes_occurred = True

            # If no changes occurred, stop the simulation
            if not changes_occurred:
                break

            # Update the states of the cells after a day of illness
            for row in range(self.n):
                for col in range(self.m):
                    if self.grid[row][col] == 'ill':
                        self.grid[row][col] = 'immune'

        return self.grid



    def get_neighbors(self, row, col):
        # Implement code to get the neighbors of a given cell (row, col) in the grid
        # Return a list of neighboring cell coordinates
        
        neighbors = []

        # Check the cell above
        if row > 0:
            neighbors.append((row - 1, col))

        # Check the cell below
        if row < self.n - 1:
            neighbors.append((row + 1, col))

        # Check the cell to the left
        if col > 0:
            neighbors.append((row, col - 1))

        # Check the cell to the right
        if col < self.m - 1:
            neighbors.append((row, col + 1))

        return neighbors

    # Additional helper methods or properties as needed

