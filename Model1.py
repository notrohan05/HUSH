# Create a 3x3 grid (0 = Empty, 1 = Obstacle)
grid = [
    [0,0,0],
    [1,1,0],
    [0,0,0]
] 

# Initialize starting position, goal and internal state
agent = [0,0]
goal = [1,2]
internal_state = []

print("agent start at:",agent)

# Continue until agent reaches the goal
while agent != goal:

    # Store current position in internal state
    internal_state.append(agent.copy())

    # Get current row and column
    row = agent[0]
    col = agent[1]

    # Check if right cell is free
    if col + 1 < 3 and grid[row][col+1] == 0:
        agent[1] = agent[1] + 1

    # If right is blocked, check downward cell
    elif row + 1 < 3 and grid[row + 1][col] == 0:
        agent[0] = agent[0] + 1

    # If both directions are blocked, stop
    else:
        print("agent is blocked",agent)
        break

    # Display updated agent position
    print("agent moved to",agent)

# Check whether the goal is reached
if agent == goal:
    print("agent reached goal",agent)

# Display all previously visited positions
print("internal state",internal_state)


# Aim
# To implement a Model-Based Intelligent Agent capable of navigating a 3x3 grid environment with obstacles using an internal state representation.

# Objectives
# 1. To understand the working of a Model-Based Intelligent Agent.
# 2. To maintain an internal state of the environment.
# 3. To navigate from the starting position to the goal.
# 4. To identify and avoid obstacles.
# 5. To remember previously visited positions and make suitable decisions.

# Theory
# A Model-Based Intelligent Agent is an AI agent that maintains an internal representation of its environment to make intelligent decisions. It uses information about the current environment and its previous states to decide the next action.
# In this experiment, the agent navigates a 2D grid from a starting position [0,0] to a goal position [2,2]. The grid contains obstacles (1) and free paths (0). The agent checks available paths, avoids obstacles, and stores its previously visited positions in an internal state. It moves right whenever possible; otherwise, it tries to move down until it reaches the goal or gets blocked.

# # Algorithm
# 1. Initialize a 3×3 grid with obstacles and free cells.
# 2. Set the agent's starting position and goal position.
# 3. Initialize an empty list to store the agent's internal state.
# 4. Check the right and downward cells for possible movement.
# 5. Move to a free cell and update the internal state.
# 6. Repeat until the goal is reached or the agent gets blocked.
# 7. Display the final position and internal state.

# Conclusion:
# Thus, we successfully implemented a Model-Based Intelligent Agent using Python. The agent maintains an internal state, identifies and avoids obstacles, remembers its previously visited positions, and makes suitable movement decisions to navigate towards the goal.



1. What is the aim of this program?
The aim is to move an agent from a starting position to a goal position in a 3×3 grid while avoiding obstacles.

2. What is an AI Agent?
An AI Agent is an entity that observes its environment and performs actions to achieve a specific goal.

3. What is an environment in this program?
The 3×3 grid is the environment in which the agent moves.

4. What do 0 and 1 represent in the grid?
- 0 represents an empty cell where the agent can move.
- 1 represents an obstacle where the agent cannot move.

5. What is the starting position of the agent?
The starting position is [0,0], which represents the first row and first column.

6. What is the goal position?
The goal position is [1,2], which represents the second row and third column.

7. What is an obstacle?
An obstacle is a blocked cell that prevents the agent from moving into that position.

8. What is internal state?
Internal state stores the previously visited positions of the agent so that its movement can be tracked.

9. Why do we use while agent != goal?
It repeats the movement process until the agent reaches the goal position.

10. Why do we use agent.copy()?
It creates a copy of the current agent position so that previously visited positions are stored correctly.

11. What is the use of len() or boundary checking in this program?
Boundary checking ensures that the agent does not move outside the grid.

12. Which directions can the agent move in?
The agent can move in two directions:
- Right
- Down

13. What happens if the right cell is blocked?
The agent checks whether the downward cell is free. If it is free, the agent moves down.
  
14. What happens if both right and downward cells are blocked?
The agent prints "agent is blocked" and stops moving using the break statement.
  
15. What is the use of break?
The break statement immediately terminates the while loop.
  
16. What is the use of elif?
elif checks another condition when the previous if condition is false.

17. What is a condition in Python?
A condition is an expression that returns either True or False.

18. What is a list in Python?
A list is a collection of elements stored in a single variable. Example: [0,0,0].

19. What is a nested list?
A nested list is a list containing other lists. Here, the 3×3 grid is a nested list.

20. What is the use of append()?
The append() function adds a new element to the end of a list.

21. What is the use of print()?
The print() function displays output on the screen.

22. What is the use of ==?
It is a comparison operator used to check whether two values are equal.

23. What is the use of and?
The and operator returns True only when both conditions are True.
  
24. What is the difference between if and elif?
- if checks the first condition.
- elif checks another condition if the previous condition is false.
  
25. What is the final output of this program?
agent start at: [0, 0]
agent moved to [0, 1]
agent moved to [0, 2]
agent moved to [1, 2]
agent reached goal [1, 2]
internal state [[0, 0], [0, 1], [0, 2]]
