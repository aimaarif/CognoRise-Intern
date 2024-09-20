import streamlit as st
import numpy as np

# Function to solve Sudoku puzzle
def solve_sudoku(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for num in range(1, 10):
        if valid_move(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

# Function to find empty cell in Sudoku puzzle
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

# Function to check if a move is valid
def valid_move(board, num, pos):
    # Check row
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 3x3 square
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True

# Function to display Sudoku board
def display_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            st.write("- - - - - - - - - - - - -")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                st.write(" | ", end="")

            if j == 8:
                st.write(board[i][j])
            else:
                st.write(str(board[i][j]) + " ", end="")

# Streamlit UI
def main():
    st.title("Sudoku Solver")

    # Create Sudoku board input matrix
    board = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            board[i][j] = st.number_input(f"Row {i+1}, Column {j+1}", min_value=0, max_value=9, key=(i, j))

    solve_button = st.button("Solve Sudoku")

    if solve_button:
        if solve_sudoku(board):
            st.success("Sudoku solved successfully!")
            display_board(board)
        else:
            st.error("No solution exists for the given Sudoku puzzle.")

if __name__ == "__main__":
    main()
