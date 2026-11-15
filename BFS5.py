from collections import deque

# 0 = Empty, 1 = Obstacle
grid = [
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 0] 
]

# Starting and goal positions
start = (0, 0)
goal = (3, 3)

# BFS function
def bfs():

    # Create queue and store starting position
    queue = deque([[start]])

    # Store visited positions
    visited = {start}

    while queue:

        # Remove first path from queue (FIFO)
        path = queue.popleft()

        # Get current position
        x, y = path[-1]

        # Check if goal is reached
        if (x, y) == goal:
            return path

        # Four possible movements: down, up, right, left
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dx, dy in moves:

            # Calculate new position
            nx = x + dx
            ny = y + dy

            # Check grid boundaries
            if 0 <= nx < 4 and 0 <= ny < 4:

                # Check obstacle and visited position
                if grid[nx][ny] == 0 and (nx, ny) not in visited:

                    # Mark position as visited
                    visited.add((nx, ny))

                    # Add new path to queue
                    queue.append(path + [(nx, ny)])

    # Return None if no path exists
    return None


# Find and display path
path = bfs()

if path:
    print("Path Found:")

    # Display each position in the path
    for position in path:
        print(position)

    # Display total number of moves
    print("Total Moves:", len(path) - 1)

else:
    print("No Path Found!")


# Aim
# To implement Breadth First Search (BFS) to solve a robot path-planning problem in Python using a grid containing obstacles.

# Objectives
# 1. To understand the working of the BFS algorithm.
# 2. To maintain a queue of positions to explore.
# 3. To find a path from the starting position to the goal.
# 4. To identify and avoid obstacles.
# 5. To find the shortest path in an unweighted grid.

# Theory
# Breadth First Search (BFS) is an uninformed search algorithm that explores nodes level by level. It uses a queue (FIFO - First In, First Out) to store positions waiting to be explored.
# In this experiment, the robot navigates a 4x4 grid from the starting position (0,0) to the goal position (3,3). The grid contains empty cells (0) and obstacles (1). BFS explores four possible directions: up, down, left, and right. It maintains a visited set to avoid visiting the same position repeatedly and finds the shortest path to reach the goal.

# Algorithm
# 1. Create a 4x4 grid with empty cells and obstacles.
# 2. Initialize the starting and goal positions.
# 3. Create a queue and add the starting position.
# 4. Mark the starting position as visited.
# 5. Remove the first path from the queue.
# 6. Check whether the goal is reached.
# 7. Explore all four possible directions.
# 8. Add valid and unvisited positions to the queue.
# 9. Repeat until the goal is found or the queue becomes empty.
# 10. Display the shortest path and total moves.

# Conclusion
# Thus, we successfully implemented Breadth First Search (BFS) using Python. The algorithm explores the grid level by level, avoids obstacles, prevents repeated visits, and finds the shortest path from the starting position to the goal.



1. What is the aim of this program?
The aim is to find the shortest path from a starting position to a goal position in a 4×4 grid while avoiding obstacles using BFS.

2. What is BFS?
BFS stands for Breadth-First Search. It is a search algorithm that explores all neighbouring nodes level by level.

3. Which algorithm is used in this program?
Breadth-First Search (BFS).

4. What does 0 represent in the grid?
0 represents an empty cell where the agent can move.

5. What does 1 represent?
1 represents an obstacle or blocked cell.

6. What is the starting position?
The starting position is (0, 0).

7. What is the goal position?
The goal position is (3, 3).

8. What is the size of the grid?
The grid size is 4×4, containing 16 cells.

9. What are the possible movements?
The agent can move in four directions:
- Down
- Up
- Right
- Left

10. Why is BFS used in this program?
BFS is used because it finds the shortest path when all movements have equal cost.

2. Python Code-Based Viva Questions

11. Why do we import deque?
We import deque from the collections module to implement an efficient queue.

12. What is a queue?
A queue is a data structure that follows FIFO (First In, First Out).

13. What is FIFO?
FIFO means the element inserted first is removed first.

14. What is the use of deque()?
It creates a double-ended queue that allows efficient insertion and deletion of elements.

15. What is the use of queue.popleft()?
It removes and returns the first element from the queue.

16. What is the use of queue.append()?
It adds a new element at the end of the queue.

17. Why do we use visited?
It stores already visited positions to avoid visiting the same position repeatedly.

18. What is the use of path[-1]?
It returns the last position in the current path, which represents the agent's current position.

19. What is the use of x, y = path[-1]?
It extracts the row and column values of the current position.

20. What is the use of for dx, dy in moves?
It checks all four possible movement directions one by one.

21. What is the use of nx = x + dx?
It calculates the new row position.

22. What is the use of ny = y + dy?
It calculates the new column position.

23. What is the use of visited.add()?
It adds a newly visited position to the visited set.

24. What is the use of queue.append(path + [(nx, ny)])?
It adds a new path containing the previous path and the newly visited position to the queue.

25. What does return None mean?
It indicates that no valid path was found.

3. Important BFS Algorithm Questions
These are particularly important for your AI viva.

26. Explain how BFS works in this program.
BFS works in the following steps:
1. Start from the initial position.
2. Insert the starting position into the queue.
3. Remove the first path from the queue.
4. Check whether the current position is the goal.
5. Explore all four neighbouring positions.
6. Ignore obstacles and already visited positions.
7. Add valid positions to the queue.
8. Repeat until the goal is reached or the queue becomes empty.

27. What is the difference between BFS and DFS?
BFS	DFS
Breadth-First Search	Depth-First Search
Uses Queue	Uses Stack
Follows FIFO	Follows LIFO
Explores level by level	Explores depth-wise
Finds shortest path in an unweighted graph	Does not guarantee shortest path


28. Is BFS informed or uninformed search?
BFS is an uninformed search algorithm because it does not use a heuristic function.

29. Is BFS complete?
Yes, BFS is complete for finite branching spaces.

30. Is BFS optimal?
Yes, BFS is optimal when all movements have equal cost.

31. What is the time complexity of BFS?
The time complexity is O(V + E), where V represents vertices and E represents edges.

32. What is the space complexity of BFS?
The space complexity is O(V), where V represents the number of vertices.

33. Why do we use a visited set?
To avoid repeated exploration and prevent infinite loops.

34. What happens if the goal is not reachable?
The queue becomes empty, and the function returns None.

35. What is pathfinding?
Pathfinding is the process of finding a valid route from a starting position to a destination.

4. Grid and Logic-Based Viva Questions

36. How does the program avoid obstacles?
It checks whether the grid cell contains 0 before moving into that position.

37. How does the program check grid boundaries?
It uses:
0 <= nx < 4 and 0 <= ny < 4
This ensures that the agent stays inside the 4×4 grid.

38. What is a neighbour in this program?
A neighbour is an adjacent cell that can be reached by moving up, down, left, or right.

39. Why are diagonal movements not allowed?
Because the program defines only four possible movements and does not include diagonal directions.

40. What is a 2D list?
A 2D list is a collection of elements arranged in rows and columns.

41. What is the purpose of moves?
It stores the four possible movement directions using row and column changes.

42. Why do we use tuples for positions?
Tuples store row and column positions together and can be used as elements of a set.

5. Output-Based Viva Questions

43. What is the output of this program?
Starting position: (0, 0)
Goal position: (3, 3)
One possible shortest path is:
Path Found:
(0, 0)
(1, 0)
(1, 1)
(2, 1)
(2, 2)
(2, 3)
(3, 3)
Total Moves: 6
Note: BFS finds a shortest path, but the exact path can depend on the order in which movements are checked.

44. How many moves are required to reach the goal?
6 moves.

45. Why do we use len(path) - 1?
Because the path contains both the starting and ending positions. The number of moves is one less than the number of positions.

46. Does BFS always find the shortest path?
Yes, provided all movements have equal cost.

47. Can the agent move through an obstacle?
No. The program checks whether the cell contains 0 before adding it to the queue.
