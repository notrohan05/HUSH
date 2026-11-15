import heapq

# Initialize starting and goal states
start = (1,2,3,4,0,6,7,5,8)
goal = (1,2,3,4,5,6,7,8,0)

# Heuristic: Count misplaced tiles (excluding 0)
def heuristic(state):
    return sum(state[i] != goal[i] and state[i] != 0 for i in range(9))

# A* Search function
def astar():

    # Store cost, moves, state and path in priority queue
    queue = [(heuristic(start), 0, start, [start])]

    # Store already visited states
    visited = set()

    while queue:

        # Get state with lowest cost
        cost, moves, state, path = heapq.heappop(queue)

        # Check if goal is reached
        if state == goal:
            print("Solution Found!")

            # Display solution path
            for s in path:
                print(s[:3])
                print(s[3:6])
                print(s[6:])
                print()

            print("Total Moves:", moves)
            return

        # Skip already visited states
        if state in visited:
            continue

        # Mark current state as visited
        visited.add(state)

        # Find position of empty tile (0)
        zero = state.index(0)

        # Four possible movements: up, down, left, right
        for move in [-3, 3, -1, 1]:

            # Calculate new position
            new = zero + move

            # Check grid boundary
            if 0 <= new < 9:

                # Prevent moving left outside the row
                if move == -1 and zero % 3 == 0:
                    continue

                # Prevent moving right outside the row
                if move == 1 and zero % 3 == 2:
                    continue

                # Swap empty tile with adjacent tile
                temp = list(state)
                temp[zero], temp[new] = temp[new], temp[zero]

                # Convert list back to tuple
                new_state = tuple(temp)

                # Check if new state is not visited
                if new_state not in visited:

                    # Calculate actual cost and total cost
                    g = moves + 1
                    f = g + heuristic(new_state)

                    # Add new state to priority queue
                    heapq.heappush(queue, (f, g, new_state, path + [new_state]))

    # If no solution exists
    print("No Solution Found!")


# Call A* Search function
astar()

# Aim
# To implement the A* Search algorithm to solve the 8-puzzle problem using Python with a heuristic function.

# Objectives
# 1. To understand the working of the A* Search algorithm.
# 2. To find a path from the initial state to the goal state.
# 3. To calculate the heuristic cost using misplaced tiles.
# 4. To generate possible puzzle states by moving the empty tile.
# 5. To find the solution with minimum moves.

# Theory
# A* is an informed search algorithm that finds the optimal path using the actual cost and heuristic cost. It uses a priority queue to select the state with the lowest total cost.
# In this experiment, the 8-puzzle consists of 8 numbered tiles and one empty space (0). The objective is to arrange the tiles in the correct order by moving the empty space up, down, left, or right.
# The heuristic function counts the number of misplaced tiles, excluding the empty space. A* uses the formula f(n) = g(n) + h(n), where g(n) is the actual number of moves and h(n) is the estimated cost to reach the goal.

# Algorithm
# 1. Initialize the starting state and goal state.
# 2. Calculate the heuristic cost using misplaced tiles.
# 3. Create a priority queue and add the starting state.
# 4. Select the state with the lowest total cost.
# 5. Check whether the goal state is reached.
# 6. Generate new states by moving the empty tile in four directions.
# 7. Calculate the new cost and add unvisited states to the queue.
# 8. Repeat until the goal is reached or no solution exists.
# 9. Display the solution path and total moves.

# Conclusion
# Thus, we successfully implemented the A* Search algorithm to solve the 8-puzzle problem using Python. The algorithm uses a heuristic function and actual path cost to explore possible states and find an optimal solution with minimum moves.



YOOO! 🔥 This program implements the A (A-Star) Search Algorithm to solve the 8-Puzzle Problem*.



1. What is the aim of this program?
The aim is to solve the 8-Puzzle Problem using the A* Search Algorithm by moving tiles into their correct positions.

2. What is the 8-Puzzle Problem?
It is a puzzle consisting of 8 numbered tiles and one empty space arranged in a 3×3 grid. The objective is to arrange the tiles in the correct order.
  
3. What is A* Search Algorithm?
A* is an informed search algorithm that finds an optimal path from the initial state to the goal state using a cost function.

4. What is a heuristic function?
A heuristic function estimates how far the current state is from the goal state.

5. Which heuristic is used in this program?
This program uses the Misplaced Tiles Heuristic, which counts the number of tiles that are not in their correct positions, excluding 0.

6. What is the difference between A* and BFS?
- BFS explores nodes level by level.
- A* uses actual cost and heuristic cost to select the most promising node.

7. What does 0 represent in this program?
0 represents the empty space in the puzzle.

8. What is the initial state?
The initial state is:
(1,2,3,4,0,6,7,5,8)

9. What is the goal state?
The goal state is:
(1,2,3,4,5,6,7,8,0)

10. What are the possible movements of the empty tile?
The empty tile can move in four directions:
- Up
- Down
- Left
- Right

11. Why do we import heapq?
We import heapq to implement a priority queue that selects the state with the lowest cost.

12. What is a priority queue?
A priority queue is a data structure in which elements are removed according to their priority.

13. What is the use of heapq.heappush()?
It inserts a new element into the priority queue.

14. What is the use of heapq.heappop()?
It removes and returns the element with the lowest priority value (smallest value).

15. Why do we use tuples for states?
Tuples are immutable, meaning their values cannot be changed directly. They can also be stored in a set.

16. Why do we use set()?
We use a set to store visited states and avoid processing the same state repeatedly.

17. What is the use of state.index(0)?
It finds the position of the empty tile (0) in the current state.

18. What is the use of list(state)?
It converts the tuple into a list so that we can swap the positions of tiles.
  
19. What is the use of tuple(temp)?
It converts the modified list back into a tuple.

20. What is the use of temp[zero], temp[new] = temp[new], temp[zero]?
It swaps the empty tile with its adjacent tile.

21. What is the use of continue?
It skips the current iteration and moves to the next iteration of the loop.

22. What is the use of return?
It terminates the function after finding and displaying the solution.

23. Why do we use path + [new_state]?
It stores the new state along with all previously visited states in the current solution path.
  
24. What is the use of while queue?
It continues searching as long as the priority queue contains unexplored states.
  
3. Important A* Algorithm Questions
  These are particularly important for your AI viva.
  
25. What is the evaluation function of A*?
The evaluation function is:
f(n) = g(n) + h(n)
Where:
- f(n) = Total estimated cost.
- g(n) = Actual cost from the starting state.
- h(n) = Estimated cost from current state to goal.

26. What is g(n) in this program?
g(n) represents the actual number of moves taken from the initial state to the current state.

27. What is h(n) in this program?
h(n) represents the number of misplaced tiles in the current state.

28. What is f(n) in this program?
It is the sum of actual cost and heuristic cost.
f = g + h

29. Is A* an informed or uninformed search algorithm?
A* is an informed search algorithm because it uses a heuristic function to guide the search.

30. Is A* complete?
Yes, A* is complete under standard conditions, such as finite branching and suitable positive step costs.
  
31. Is A* optimal?
Yes, A* is optimal when an appropriate admissible heuristic is used.

32. What is an admissible heuristic?
An admissible heuristic never overestimates the actual minimum cost required to reach the goal.
  
33. Is the heuristic used in this program admissible?
Yes. The misplaced tiles heuristic never overestimates the minimum number of moves required to reach the goal.

34. What is the difference between Greedy Best First Search and A*?
- Greedy Best First Search uses only h(n).
- A* uses both g(n) and h(n).

35. What is the use of the visited set?
It prevents the algorithm from processing the same puzzle state repeatedly.
