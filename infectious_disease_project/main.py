import cellular_automaton
import animation
import numpy as np

def get_user_input():
    n = int(input("Enter the number of rows in the dormitory: "))
    m = int(input("Enter the number of columns in the dormitory: "))
    initial_bed = input("Enter the initial infected bed position (in the format 'row,column'): ")
    initial_bed = tuple(map(int, initial_bed.split(',')))
    p = float(input("Enter the probability of infection (0 < p < 1): "))
    k = int(input("Enter the duration of illness (in days): "))
    repetitions = int(input("Enter the number of repetitions: "))
    return n, m, initial_bed, p, k, repetitions

def main():
    n, m, initial_bed, p, k, repetitions = get_user_input()
    grid = cellular_automaton.initialize_grid(n, m, initial_bed)
    grid_list = [grid.copy()]

    for _ in range(repetitions):
        grid = cellular_automaton.simulate_spread(grid, p, k)
        grid_list.append(grid.copy())

    for grid in grid_list:
        print(grid)
        print()

    animation.generate_animation(grid_list)

    

if __name__ == "__main__":
    main()
