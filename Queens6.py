# 8 Queens using Backtracking

N = 8

# Create an empty chessboard
board = [[0 for i in range(N)] for j in range(N)]


# Check whether queen can be placed safely
def safe(row, col):

    for i in range(row):

        # Check same column
        if board[i][col] == 1:
            return False

        # Check left diagonal
        if col - (row - i) >= 0:
            if board[i][col - (row - i)] == 1:
                return False

        # Check right diagonal
        if col + (row - i) < N:
            if board[i][col + (row - i)] == 1:
                return False

    return True


# Solve the problem using backtracking
def solve(row):

    # All queens are placed
    if row == N:
        return True

    # Try every column in the current row
    for col in range(N):

        if safe(row, col):

            # Place queen
            board[row][col] = 1

            # Move to the next row
            if solve(row + 1):
                return True

            # Remove queen if solution is not found
            board[row][col] = 0

    return False


# Display the solution
if solve(0):
    print("Solution Found!")
    for row in board:
        print(row)
else:
    print("No Solution Found!")


# Aim
# To implement Backtracking Search to solve the 8-Queens Constraint Satisfaction Problem using Python.

# Objectives
# 1. To understand the backtracking search algorithm.
# 2. To place 8 queens on a chessboard.
# 3. To ensure that no two queens attack each other.
# 4. To find a valid solution using constraints.

# Theory
# The 8-Queens problem is a chess puzzle in which 8 queens must be placed on an 8×8 chessboard so that no two queens attack each other.
# No two queens should be in the same row, column, or diagonal. Backtracking tries different positions and removes a queen whenever a constraint is violated. It continues until a valid arrangement is found.

# Algorithm
# 1. Start the program.
# 2. Create an 8×8 chessboard.
# 3. Place a queen in the first row.
# 4. Check whether the position is safe.
# 5. If safe, place the queen and move to the next row.
# 6. Repeat until all 8 queens are placed.
# 7. If no safe position is available, remove the previously placed queen and try another position.
# 8. Display the solution when all queens are placed.
# 9. Stop the program.

# Conclusion
# Thus, we successfully implemented the 8-Queens problem using Backtracking Search in Python. The program places 8 queens on the chessboard while satisfying all constraints and ensuring that no two queens attack each other.




1. What is the aim of this program?
The aim is to place 8 queens on an 8×8 chessboard so that no two queens attack each other.

2. What is the 8 Queens Problem?
It is a chess puzzle in which 8 queens must be placed on an 8×8 chessboard without attacking each other.
  
3. Which algorithm is used in this program?
Backtracking Algorithm.

4. What is Backtracking?
Backtracking is a problem-solving technique in which we try a possible solution and go back if that solution does not work.

5. What is a queen in chess?
A queen is a chess piece that can move horizontally, vertically, and diagonally.

6. What are the conditions for placing queens?
Three conditions must be satisfied:
1. No two queens should be in the same row.
2. No two queens should be in the same column.
3. No two queens should be on the same diagonal.
  
7. What does 1 represent in the chessboard?
1 represents the position where a queen is placed.

8. What does 0 represent?
0 represents an empty cell.

9. What is the size of the chessboard?
The chessboard is 8×8, containing 64 cells.
  
10. How many queens are placed?
Exactly 8 queens.

2. Python Code-Based Viva Questions
  
11. What is the use of N = 8?
It defines the size of the chessboard as 8×8.

12. What is the use of this statement?
board = [[0 for i in range(N)] for j in range(N)]
It creates an 8×8 chessboard filled with zeros.

13. What is a 2D list?
A 2D list is a collection of elements arranged in rows and columns.

14. What is the use of the safe() function?
It checks whether a queen can be safely placed at a particular row and column.
  
15. What are the parameters of safe(row, col)?
- row represents the current row.
- col represents the column where we want to place the queen.
  
16. Why do we use range(row)?
It checks all the previous rows to find whether another queen is attacking the current position.
  
17. What is the use of return False?
It indicates that the selected position is unsafe for placing a queen.
  
18. What is the use of return True?
It indicates that the selected position is safe for placing a queen.

19. What is the use of board[row][col] = 1?
It places a queen at the selected position.

20. What is the use of board[row][col] = 0?
It removes the queen when the selected arrangement does not lead to a solution.

21. What is recursion?
Recursion is a process in which a function calls itself.

22. Which function uses recursion?
The solve() function calls itself to place queens in the next row.

23. What is the use of solve(row + 1)?
It moves to the next row to place the next queen.

24. What is the use of for col in range(N)?
It tries all 8 columns in the current row to find a safe position.

25. What is the use of if row == N?
It checks whether all 8 queens have been successfully placed.

26. What is the use of return?
It exits the function and returns a value.

3. Important Backtracking Questions
These are particularly important for your AI viva.
                                
27. Explain how Backtracking works in this program.
Backtracking works in the following steps:
1. Start from the first row.
2. Try placing a queen in each column.
3. Check whether the position is safe.
4. If safe, place the queen.
5. Move to the next row.
6. If no safe position is available, remove the previous queen.
7. Try another position.
8. Repeat until all 8 queens are placed.

28. Why is Backtracking used in the 8 Queens Problem?
Because it helps find a valid arrangement by trying different positions and removing incorrect choices.

29. What is the base condition in this program?
When row == N, all 8 queens are placed successfully, and the function returns True.

30. What is pruning?
Pruning means eliminating invalid possibilities without exploring them further.

31. How does the program check the same column?
It checks whether any previous row contains a queen in the same column.

32. How does the program check the left diagonal?
It checks the upper-left diagonal of the current position.
  
33. How does the program check the right diagonal?
It checks the upper-right diagonal of the current position.

34. Why does the program only check previous rows?
Because the algorithm places queens row by row, so queens can only exist in previous rows when checking a new position.

35. What happens if a queen cannot be placed in any column?
The algorithm returns False and goes back to the previous row to try another position.

4. Logic-Based Viva Questions
  
36. Why can two queens not be placed in the same column?
Because queens can attack each other vertically.
  
37. Why can two queens not be placed diagonally?
Because queens can attack each other diagonally.

38. Why are two queens never placed in the same row?
Because the program places only one queen in each row before moving to the next row.

39. What is the purpose of col - (row - i) >= 0?
It checks whether the upper-left diagonal position is within the chessboard boundary.

40. What is the purpose of col + (row - i) < N?
It checks whether the upper-right diagonal position is within the chessboard boundary.

41. Can the 8 Queens Problem have multiple solutions?
Yes. The 8 Queens Problem has 92 different solutions.

42. Does this program display all solutions?
No. It displays only the first valid solution because it returns True as soon as a solution is found.

43. What is the time complexity of the 8 Queens Problem?
The worst-case time complexity is exponential because the algorithm explores different possible queen placements.
  
5. Output-Based Viva Questions
  
44. What is the output of this program?
One possible output is:
Solution Found!
[1, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1]
[0, 0, 0, 0, 0, 1, 0, 0]
[0, 0, 1, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 1, 0]
[0, 1, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 1, 0, 0, 0, 0]

45. How many queens are present in the final solution?
8 queens.

46. Why does the program print "Solution Found!"?
Because all 8 queens are successfully placed without attacking each other.

47. What happens if no solution is found?
The program prints "No Solution Found!"
