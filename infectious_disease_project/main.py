import cellular_automaton
import animation
import numpy as np

def get_user_choice():
    c = int(input("Enter the number of your choice:\n1: Normal Execute\n2: Add Vaccination\n3: Add Bed Swap "))
    return c

def get_user_input():
    n = int(input("Enter the number of rows in the dormitory: "))
    m = int(input("Enter the number of columns in the dormitory: "))
    initial_bed = input("Enter the initial infected bed position (in the format 'row,column'): ")
    initial_bed = tuple(map(int, initial_bed.split(',')))
    p = float(input("Enter the probability of infection (0 < p < 1): "))
    k = int(input("Enter the duration of illness (in days): "))
    repetitions = int(input("Enter the number of repetitions: "))
    return n, m, initial_bed, p, k, repetitions

def get_user_input_vaccines():
    v = int(input("Enter the number of vaccines per day: "))
    return v

def get_user_input_bedSwap():
    bs = int(input("Enter the number of Bed Swaps you want to perform per day: "))
    return bs

def main():
    c = get_user_choice()
    n, m, initial_bed, p, k, repetitions = get_user_input()
    grid = cellular_automaton.initialize_grid(n, m, initial_bed, k)
    grid_list = [grid.copy()]

    if c == 1:
        for _ in range(repetitions):
            grid = cellular_automaton.simulate_spread(grid, p, k)
            grid_list.append(grid.copy())
    elif c == 2:
        v = get_user_input_vaccines()
        for _ in range(repetitions):
            grid = cellular_automaton.simulate_spread_vaccines(grid, p, k, v)
            grid_list.append(grid.copy())
    elif c == 3:
        v = get_user_input_vaccines()
        bs = get_user_input_bedSwap()
        for _ in range(repetitions):
            grid = cellular_automaton.simulate_spread_bed_swap(grid, p, k, v, bs)
            grid_list.append(grid.copy())

    for grid in grid_list:
        print(grid)
        print()

    animation.generate_animation(grid_list)

    

if __name__ == "__main__":
    main()
