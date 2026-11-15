# To implement Goal Stack Planning for Blocks World

# Initial arrangement of blocks
blocks = {
    'A': 'table',
    'B': 'A',
    'C': 'table'
}

# Goals to be achieved
goal_stack = [
    ('C', 'B'),
    ('B', 'table'),
    ('A', 'table')
]

# Check whether a block is clear
def clear(block):
    return all(position != block for position in blocks.values())


# Function to solve the problem
def solve():

    # Continue until all goals are checked
    while goal_stack:

        # Get the next goal from the stack
        block, destination = goal_stack.pop()

        # Skip if the block is already in the correct position
        if blocks[block] == destination:
            continue

        # Check whether the block and destination are clear
        if clear(block) and (destination == 'table' or clear(destination)):

            # Store the old position
            old = blocks[block]

            # Move the block to its destination
            blocks[block] = destination

            # Display the movement
            print("Moved", block, "from", old, "to", destination)

    # Check whether the goal state is achieved
    if blocks == {'A': 'table', 'B': 'table', 'C': 'B'}:
        print("Goal State Reached!")
    else:
        print("Goal State Not Reached!")

    # Display the final arrangement
    print("Final State:", blocks)


# Execute the program
solve()

# Aim
# To implement Goal Stack Planning for the Blocks World problem using Python.

# Objectives
# 1. To understand Goal Stack Planning.
# 2. To arrange blocks in the required positions.
# 3. To check whether blocks can be moved safely.
# 4. To achieve the goal state.

# Theory
# Goal Stack Planning is an AI technique that uses a stack to achieve a goal.
# In Blocks World, blocks are moved from one position to another.
# The program checks block positions and performs valid movements
# until the required arrangement is achieved.

# Algorithm
# 1. Start the program.
# 2. Define the initial block arrangement.
# 3. Define the goal stack.
# 4. Check whether a block is clear.
# 5. Move the block if the movement is valid.
# 6. Repeat until all goals are checked.
# 7. Display the final state.
# 8. Stop the program.

# Conclusion
# Thus, we successfully implemented Goal Stack Planning
# to arrange blocks according to the given goal state using Python.



Q1. What is Goal Stack Planning?
Goal Stack Planning is an AI planning technique in which goals are stored in a stack and solved one by one to reach the desired final state.

Q2. What is Blocks World?
Blocks World is a problem in Artificial Intelligence where blocks are arranged on a table or placed on top of other blocks.

Q3. What is the purpose of this program?
The purpose is to rearrange blocks from their initial arrangement into the required goal arrangement using Goal Stack Planning.

Q4. What is the initial state in your program?
The initial arrangement is:
- A is on the table.
- B is on A.
- C is on the table.
  
Q5. What is the goal state?
The goal state is:
- A is on the table.
- B is on the table.
- C is on B.

Q6. What is a goal stack?
A goal stack is a data structure that stores the goals that need to be achieved.

Q7. Which data structure is used for the goal stack?
A Python list is used as a stack.

Q8. What is LIFO?
LIFO means Last In, First Out. The last element inserted into a stack is removed first.
2. Python Code-Based Viva Questions
Q9. Why is a dictionary used in this program?
A dictionary is used to store the current position of each block.
Example:
blocks = {    'A': 'table',    'B': 'A',    'C': 'table'}
It means B is placed on A.

Q10. What does goal_stack.pop() do?
It removes and returns the last goal from the stack.

Q11. What is the purpose of the clear() function?
It checks whether a block has another block placed on top of it.

Q12. Explain this statement:
return all(position != block for position in blocks.values())
It checks whether any block is placed on the given block.
- If no block is placed on it, it returns True.
- If another block is placed on it, it returns False.
  
Q13. What is the purpose of the while goal_stack loop?
It continues processing goals until the goal stack becomes empty.

Q14. What does continue do?
It skips the remaining statements in the current iteration and moves to the next iteration of the loop.

Q15. Why do we use if blocks[block] == destination?
It checks whether the block is already at its required destination. If yes, no movement is needed.

Q16. What is the purpose of the old variable?
It stores the previous position of the block before moving it.

Q17. What does this statement do?
blocks[block] = destination
It updates the position of the block to its new destination.

3. Algorithm and AI-Based Viva Questions

Q18. What is the main concept behind Goal Stack Planning?
The main concept is to break a problem into smaller goals and achieve them one by one.

Q19. What are the conditions required to move a block?
1. The block to be moved must be clear.
2. The destination must be clear.
3. The destination can also be the table.

Q20. What does clear mean in Blocks World?
A block is clear if no other block is placed on top of it.

Q21. What is a goal state?
A goal state is the final arrangement that we want to achieve.

Q22. What is a state space?
State space is the collection of all possible arrangements of blocks in a problem.

Q23. Is Goal Stack Planning an AI planning technique?
Yes. It is a classical AI planning technique used to achieve a desired goal state.

Q24. What is the difference between initial state and goal state?  
- Initial state: The starting arrangement of blocks.
- Goal state: The required final arrangement of blocks.
  
4. Logic-Based Viva Questions
  
Q25. Which block is moved first in this program?
Block B is moved first because the last goal added to the list is removed first, and the first popped goal is ('A', 'table'), which is already satisfied. The next goal is ('B', 'table').

Q26. Why is B moved from A to the table?
Because B is clear, and the table is always available as a destination.

Q27. Why can C be placed on B?
After moving B to the table, B becomes clear. C is also clear, so C can be placed on B.

Q28. Why is A not moved?
Because A is already on the table, which is its required destination.

Q29. What happens if a block is not clear?
The movement condition becomes false, so the program does not perform that movement.

Q30. Does this program implement complete Goal Stack Planning?
It demonstrates a simplified version of Goal Stack Planning. A complete implementation would also handle action preconditions, subgoals and situations where a movement cannot be performed.

5. Output-Based Viva Questions

Q31. What is the output of this program?
Moved B from A to table
Moved C from table to B
Goal State Reached!
Final State: {'A': 'table', 'B': 'table', 'C': 'B'}

Q32. How many blocks are used in this program?
Three blocks: A, B and C.

Q33. How many movements are performed?
Two movements.

Q34. What is the final arrangement?
A and B are on the table, and C is placed on B.

Q35. What happens if the goal state is not achieved?
The program prints:
Goal State Not Reached!
