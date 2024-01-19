import numpy as np  # Importing NumPy, a library used for numerical operations and handling arrays

# Function to check if placing a queen at a given row and column is safe
def is_safe(board, row, col, n):
    # Check for conflicts with other queens in the same row or diagonals
    for i in range(col):
        # If another queen is in the same row or diagonal, it's not safe
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True  # If no conflicts, it's safe to place the queen

# Backtracking algorithm to solve N-Queens
def solve_n_queens_backtracking(board, col, n, solutions):
    # Check if all queens are placed (base case)
    if col >= n:
        solutions.append(board.copy())  # Add the current board arrangement to solutions
        return

    # Try placing a queen in each row of the current column
    for i in range(n):
        if is_safe(board, i, col, n):  # Check if placing the queen here is safe
            board[col] = i  # Place the queen
            solve_n_queens_backtracking(board, col + 1, n, solutions)  # Move to the next column
            board[col] = -1  # Remove the queen (backtrack) if it leads to no solution

# Function to print the N-Queens board
def print_board(board):
    n = len(board)  # Determine the size of the board
    for row in board:  # Loop through each row of the board
        # Print 'Q' for queen and '.' for empty space, based on the row position
        print(" ".join("Q" if col == row else "." for col in range(n)))
    print()  # Print a new line after the board

# Las Vegas algorithm to solve N-Queens
def solve_n_queens_las_vegas(board, n, max_attempts):
    attempt = 0  # Initialize the attempt counter
    while attempt < max_attempts:  # Repeat until the maximum number of attempts is reached
        # Randomly place queens in each column
        board[:] = np.random.randint(0, n, size=n)
        if solve_n_queens_backtracking(board, 0, n, []):  # Check if the board is a solution
            return True  # Solution found
        attempt += 1  # Increment the attempt counter
    return False  # No solution found within the given attempts

# Function to calculate the success rate and record outcomes of each run
def calculate_success_rate_and_record_runs(n, runs, max_attempts):
    success_count = 0  # Counter for successful runs
    successful_runs = []  # List to record the numbers of successful runs

    for run in range(1, runs + 1):  # Loop for the specified number of runs
        board = [-1] * n  # Initialize the board with -1 (no queens placed)
        if solve_n_queens_las_vegas(board, n, max_attempts):  # Run the Las Vegas algorithm
            success_count += 1  # Increment the success count
            successful_runs.append(run)  # Record the successful run number

    success_rate = success_count / runs  # Calculate the success rate
    return success_rate, successful_runs, success_count  # Return the success rate and successful runs

# Function to get user input
def get_user_input():
    n = int(input("Enter the number of queens: "))  # Ask for the number of queens
    approach = input("Choose the approach (Backtracking or Las Vegas): ")  # Ask for the algorithm choice
    # Ask for specific inputs if the Las Vegas approach is chosen
    if approach == 'Las Vegas':
        max_runs = int(input("Enter the number of runs for calculating success rate: "))  # Number of runs for success rate
        max_attempts = int(input("Enter the maximum number of attempts for Las Vegas: "))  # Maximum attempts per run
    else:
        max_runs = None
        max_attempts = None
    return n, approach, max_runs, max_attempts

# Main function to run the N-Queens program
def main():
    n, approach, max_runs, max_attempts = get_user_input()  # Get the user's input

    if approach == 'Backtracking':
        board = [-1] * n  # Initialize the board for backtracking
        solutions = []  # List to store solutions
        solve_n_queens_backtracking(board, 0, n, solutions)  # Solve N-Queens using backtracking
        success_rate = 100 if solutions else 0  # Calculate the success rate (100% if solutions are found)
        print(f"{len(solutions)} solutions found for {n} queens.")  # Print the number of solutions
        print(f"Success Rate for Backtracking with {n} Queens: {success_rate}% (equation: '100%' if at least one solution is found)")
        for i, solution in enumerate(solutions, 1):
            print(f"Solution {i}:")  # Print each solution number
            print_board(solution)  # Print the board for each solution
    elif approach == 'Las Vegas':
        success_rate, successful_runs, success_count = calculate_success_rate_and_record_runs(n, max_runs, max_attempts)
        print(f"Success Rate for Las Vegas with {n} Queens: {success_rate * 100}% (equation: '{success_count}/{max_runs} * 100 = {success_rate * 100}%')")
        for i, run_number in enumerate(successful_runs, 1):
            print(f"Solution {i} - Success: run {run_number}")  # Print each successful run number

# Call the main function to run the program
if __name__ == "__main__":
    main()
