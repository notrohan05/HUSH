# 0 represents an empty cell
board = [
    [1, 0, 0, 4],
    [0, 4, 1, 0],
    [0, 1, 4, 0],
    [4, 0, 0, 1]
]

# Print original Sudoku board
print("Original Sudoku:")
for row in board:
    print(row)

# Check whether a number is valid
def valid(r, c, n):

    # Check the row and column
    for i in range(4):
        if board[r][i] == n or board[i][c] == n:
            return False

    # Check the 2x2 box
    for i in range(2):
        for j in range(2):
            if board[r//2*2+i][c//2*2+j] == n:
                return False

    # Number is valid
    return True


# Solve Sudoku using backtracking
def solve():

    # Check every row and column
    for r in range(4):
        for c in range(4):

            # Find an empty cell
            if board[r][c] == 0:

                # Try numbers from 1 to 4
                for n in range(1, 5):

                    # Check whether number is valid
                    if valid(r, c, n):

                        # Place the number
                        board[r][c] = n

                        # Solve the next empty cell
                        if solve():
                            return True

                        # Backtrack if solution is not found
                        board[r][c] = 0

                # No valid number found
                return False

    # All cells are filled
    return True


# Print solved Sudoku
if solve():
    print("\nSolved Sudoku:")
    for row in board:
        print(row)
else:
    print("No Solution!")


# Aim
# To implement a Sudoku solver using Python and the backtracking technique to solve a 4x4 Sudoku puzzle.

# Objectives
# 1. To understand the working of the backtracking algorithm.
# 2. To identify empty cells in a Sudoku grid.
# 3. To check valid numbers in rows, columns, and 2x2 boxes.
# 4. To fill empty cells with valid numbers from 1 to 4.
# 5. To solve the Sudoku puzzle by applying backtracking.

# Theory
# Sudoku is a number-placement puzzle consisting of a 4x4 grid. The objective is to fill all empty cells with numbers from 1 to 4 without repeating numbers in any row, column, or 2x2 box.
# In this experiment, the backtracking technique is used to solve the Sudoku puzzle. The program finds an empty cell and tries numbers from 1 to 4. It checks whether each number is valid according to Sudoku rules. If a number is valid, it is placed in the cell and the program moves to the next empty cell. If no valid solution is found, the program goes back, removes the previously placed number, and tries another number. This process continues until the puzzle is solved.

# Algorithm
# 1. Create a 4x4 Sudoku grid with empty cells represented by 0.
# 2. Check each row and column to find an empty cell.
# 3. Try numbers from 1 to 4 in the empty cell.
# 4. Check whether the number is valid in its row, column, and 2x2 box.
# 5. If valid, place the number and call the solve function again.
# 6. If the solution fails, reset the cell to 0 (Backtracking).
# 7. Repeat until all cells are filled.
# 8. Display the solved Sudoku or print no solution.

# Conclusion
# Thus, we successfully implemented a Sudoku solver using Python and the backtracking technique. The program checks row, column, and 2x2 box constraints, fills empty cells with valid numbers, and uses backtracking to find the correct solution.


1. What is the aim of this program?
The aim is to solve a 4×4 Sudoku puzzle by filling empty cells with valid numbers using the Backtracking Algorithm.

2. What is Sudoku?
Sudoku is a number puzzle in which numbers must be arranged according to specific rules without repetition in rows, columns, and subgrids.

3. What is a 4×4 Sudoku?
A 4×4 Sudoku consists of 16 cells arranged in 4 rows and 4 columns. It uses numbers from 1 to 4.

4. What does 0 represent in this program?
0 represents an empty cell that needs to be filled.

5. Which algorithm is used in this program?
The Backtracking Algorithm is used to solve the Sudoku puzzle.

6. What is Backtracking?
Backtracking is a problem-solving technique in which we try a possible solution and go back if that solution does not work.

7. Why is Backtracking used in Sudoku?
It helps find the correct arrangement of numbers by trying different possibilities and removing incorrect choices.

8. What are the rules of Sudoku?
There are three main rules:
1. Numbers must not repeat in the same row.
2. Numbers must not repeat in the same column.
3. Numbers must not repeat in the same 2×2 box.

9. What numbers are used in this program?
Numbers from 1 to 4 are used.

10. What is the final goal of this program?
To fill all empty cells while satisfying all Sudoku rules.

2. Python Code-Based Viva Questions

11. What is the use of a 2D list?
A 2D list stores data in rows and columns. Here, it represents the Sudoku board.

12. What is the use of print()?
It displays the Sudoku board and the final result on the screen.

13. What is the use of for loop?
It is used to repeat statements and check every row and column of the Sudoku board.

14. What is the use of range(4)?
It generates numbers from 0 to 3, representing the four rows or columns.

15. What is the use of the valid() function?
It checks whether a number can be safely placed in a particular cell without violating Sudoku rules.

16. What are the parameters of valid(r, c, n)?
- r = Row number.
- c = Column number.
- n = Number to be inserted.

17. Why do we use return False?
It indicates that the selected number is invalid.

18. Why do we use return True?
It indicates that the selected number is valid or that the Sudoku has been successfully solved.

19. What is the use of if board[r][c] == 0?
It checks whether the current cell is empty.

20. What is the use of range(1, 5)?
It generates numbers from 1 to 4 that can be placed in the empty cell.

21. What is the use of board[r][c] = n?
It places the selected number into the empty cell.

22. What is the use of board[r][c] = 0?
It removes an incorrect number during backtracking and makes the cell empty again.

23. What is recursion?
Recursion is a process in which a function calls itself to solve a problem.

24. Which function uses recursion in this program?
The solve() function calls itself recursively to solve the next empty cell.

25. What is the use of return?
It exits the function and returns a value to the calling function.

3. Important Backtracking Questions
These are particularly important for your AI viva.

26. Explain how Backtracking works in this program.
The algorithm works in the following steps:
1. Find an empty cell in the Sudoku board.
2. Try numbers from 1 to 4.
3. Check whether the number is valid.
4. If valid, place the number.
5. Call the function recursively for the next empty cell.
6. If the solution fails, remove the number and try another number.
7. Continue until the complete Sudoku is solved.

27. What is the difference between Backtracking and Brute Force?
- Brute Force tries all possible combinations.
- Backtracking eliminates invalid choices as soon as they are detected.

28. What is the use of the valid() function in Backtracking?
It prevents invalid numbers from being placed in the Sudoku board.

29. What happens when no valid number is found?
The function returns False, and the algorithm goes back to the previous cell to try another number.

30. What is the meaning of pruning?
Pruning means eliminating choices that cannot lead to a valid solution.

31. What is the base condition in this program?
When there are no empty cells left, the function returns True, indicating that the Sudoku is solved.

32. Why is recursion important in this program?
Recursion helps the algorithm move from one empty cell to the next until the puzzle is solved.

33. What is the time complexity of Backtracking?
In the worst case, it can be exponential because the algorithm may need to explore many possible combinations.

4. Sudoku Logic-Based Viva Questions

34. How does the program check the row?
It checks all four cells in the selected row to ensure the number does not already exist.

35. How does the program check the column?
It checks all four cells in the selected column to ensure the number does not already exist.

36. How does the program check the 2×2 box?
It uses nested loops to check all four cells in the corresponding 2×2 subgrid.

37. What is the meaning of r//2*2?
It calculates the starting row index of the 2×2 box containing the selected cell.

38. What is the meaning of c//2*2?
It calculates the starting column index of the 2×2 box containing the selected cell.

39. Why do we use nested loops?
Nested loops help check all cells inside the 2×2 subgrid.

40. What happens if a number already exists in the same row?
The valid() function returns False, and that number is not placed.

5. Output-Based Viva Questions

41. What is the output of this program?
Original Sudoku:
[1, 0, 0, 4]
[0, 4, 1, 0]
[0, 1, 4, 0]
[4, 0, 0, 1]

Solved Sudoku:
[1, 2, 3, 4]
[3, 4, 1, 2]
[2, 1, 4, 3]
[4, 3, 2, 1]

42. What happens if the Sudoku has no solution?
The program prints No Solution!.

43. Does this program modify the original board?
Yes. It fills the empty cells directly in the original board.

44. Can this program solve a 9×9 Sudoku?
Not directly. The current code is designed specifically for a 4×4 Sudoku. It would need modifications for a 9×9 Sudoku.


