from cellular_automaton import CellularAutomaton
from animation import generate_animation

def get_user_input():
    # Implement code to get user input for parameters
    # such as n, m, initial infected bed, probability of infection (p), duration of illness (k)
    # Return the values entered by the user
    
    n = int(input("Enter the number of rows in the dormitory: "))
    m = int(input("Enter the number of columns in the dormitory: "))
    initial_bed = input("Enter the initial infected bed position (in the format 'row,column'): ")
    p = float(input("Enter the probability of infection (0 < p < 1): "))
    k = int(input("Enter the duration of illness (in days): "))

    # Return the entered values as a tuple
    return n, m, initial_bed, p, k

def main():
    # Get user input
    n, m, initial_bed, p, k = get_user_input()

    # Initialize the cellular automaton
    automaton = CellularAutomaton(n, m, initial_bed, p, k)

    # Simulate the disease spread
    automaton.simulate_spread()

    # Generate animation
    generate_animation(automaton.grid)

if __name__ == '__main__':
    main()