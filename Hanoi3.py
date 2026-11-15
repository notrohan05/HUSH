# Tower of Hanoi using State Space Search (BFS)

# Initial and goal states
start = ((3, 2, 1), (), ())  # All disks are on rod A
goal = ((), (), (3, 2, 1))   # All disks are on rod C

# Queue stores states and paths
queue = [(start, [])]
visited = [start]  # Stores already visited states

# BFS
while queue:

    state, path = queue.pop(0)  # Get the first state from queue

    # Check if goal is reached
    if state == goal:
        print("Goal State Reached!")

        for move in path:
            print(move)

        print("Total Moves:", len(path))
        break

    # Check all possible rod movements
    for i in range(3):
        for j in range(3):

            # Check that source and destination are different
            # and source rod is not empty
            if i != j and state[i]:

                disk = state[i][-1]  # Get the top disk

                # Check if the disk can be moved
                if not state[j] or state[j][-1] > disk:

                    rods = [list(rod) for rod in state]  # Copy rods

                    # Move disk from source to destination
                    rods[i].pop()
                    rods[j].append(disk)

                    # Convert new state into tuple
                    new_state = tuple(tuple(rod) for rod in rods)

                    # Check if state is already visited
                    if new_state not in visited:
                        visited.append(new_state)

                        # Store the movement
                        move = "Move disk " + str(disk) + " from " + "ABC"[i] + " to " + "ABC"[j]

                        # Add new state and path to queue
                        queue.append((new_state, path + [move]))

else:
    print("No Solution!")

# Aim
# To implement the Tower of Hanoi problem using State Space Search (BFS) in Python.

# Objectives
# 1. To understand the concept of State Space Search.
# 2. To represent each arrangement of disks as a state.
# 3. To generate all possible valid movements between rods.
# 4. To use BFS to find the shortest path to the goal state.
# 5. To reach the goal state by following the rules of Tower of Hanoi.

# Theory
# Tower of Hanoi is a mathematical puzzle consisting of three rods and different-sized disks.
# The objective is to move all disks from the source rod to the destination rod.
# Only one disk can be moved at a time, and a larger disk cannot be placed on a smaller disk.
# In State Space Search, each arrangement of disks is considered a state.
# BFS explores these states level by level using a queue and finds the shortest sequence of valid moves.

# Algorithm
# 1. Start the program.
# 2. Initialize the initial state and goal state.
# 3. Create a queue to store states and their paths.
# 4. Create a visited list to avoid checking the same state again.
# 5. Remove the first state from the queue.
# 6. Check whether the current state matches the goal state.
# 7. Generate all possible valid disk movements between the three rods.
# 8. Create a new state after each valid movement.
# 9. Add unvisited states to the queue.
# 10. Repeat until the goal state is reached.
# 11. Display the solution and total number of moves.
# 12. Stop the program.

# Conclusion
# Thus, we successfully implemented the Tower of Hanoi problem using State Space Search (BFS) in Python.
# The program explores different states and finds the shortest sequence of valid moves to reach the goal state.



1. What is the aim of this program?
The aim is to solve the Tower of Hanoi problem by moving all disks from rod A to rod C using BFS.

2. What is Tower of Hanoi?
Tower of Hanoi is a mathematical puzzle consisting of three rods and disks of different sizes. The objective is to move all disks from the source rod to the destination rod.

3. How many rods are used in Tower of Hanoi?
Three rods:
- Rod A – Source
- Rod B – Auxiliary
- Rod C – Destination

4. Which algorithm is used in this program?
Breadth-First Search (BFS).

5. What is BFS?
BFS stands for Breadth-First Search. It explores all possible states level by level using a queue.
  
6. What is State Space Search?
State Space Search is a problem-solving technique in which a problem is represented using different states and transitions between those states.
  
7. What is a state in this program?
A state represents the current arrangement of disks on the three rods.

8. What is the initial state?
The initial state is:
((3, 2, 1), (), ())
All disks are initially placed on rod A.
  
9. What is the goal state?
The goal state is:
((), (), (3, 2, 1))
All disks are moved to rod C.

10. What are the rules of Tower of Hanoi?
1. Only one disk can be moved at a time.
2. Only the top disk can be moved.
3. A larger disk cannot be placed on a smaller disk.


11. Why do we use tuples for representing states?
Tuples represent the arrangement of disks on the rods. They also help identify and store unique states.

12. What does () represent?
It represents an empty rod.

13. What is the use of queue = [(start, [])]?
It initializes the queue with the starting state and an empty path.

14. What is the use of queue.pop(0)?
It removes and returns the first element from the queue, following FIFO order.

15. What is FIFO?
FIFO means First In, First Out. The element inserted first is removed first.

16. What is the use of visited?
It stores already visited states to avoid exploring the same state repeatedly.

17. Why do we use while queue?
It continues the search as long as there are states available in the queue.

18. What is the use of state[i][-1]?
It accesses the top disk of rod i.

19. What is the use of if i != j?
It ensures that the source rod and destination rod are different.
  
20. What is the use of if not state[j]?
It checks whether the destination rod is empty.

21. What is the use of state[j][-1] > disk?
It checks whether the top disk on the destination rod is larger than the disk being moved.

22. Why do we use list(rod)?
It converts each rod tuple into a list so that disks can be added or removed.
  
23. What is the use of pop()?
It removes the top disk from the source rod.

24. What is the use of append()?
It adds the disk to the destination rod.

25. Why do we convert the rods back into tuples?
To create an immutable state that can be compared and stored in the visited list.

26. What is the use of "ABC"[i]?
It converts the rod index into its corresponding name:
- 0 = A
- 1 = B
- 2 = C

27. What is the use of str(disk)?
It converts the disk number into a string so it can be combined with other text.
  
28. What is the use of path + [move]?
It creates a new path containing all previous moves and the current move.

29. What is the use of break?
It terminates the loop when the goal state is reached.

30. What is the use of else after the while loop?
It executes when the while loop finishes normally without encountering a break.

3. Important BFS and AI Conceptual Questions
These are particularly important for your AI viva.
                                
31. Explain how BFS works in this program.
BFS works in the following steps:
1. Initialize the starting state.
2. Insert the starting state into the queue.
3. Remove the first state from the queue.
4. Check whether it is the goal state.
5. Generate all possible valid disk movements.
6. Ignore already visited states.
7. Add new states to the queue.
8. Repeat until the goal state is reached.
                                
32. Why is BFS used in Tower of Hanoi?
BFS explores states level by level and finds the solution with the minimum number of moves.
                                
33. Is BFS informed or uninformed search?
BFS is an uninformed search algorithm because it does not use a heuristic function.
                                
34. Is BFS complete?
Yes, BFS is complete for a finite state space.
                                
35. Is BFS optimal?
Yes, BFS is optimal when every move has equal cost.

36. What is the difference between BFS and DFS?
BFS	DFS
Breadth-First Search	Depth-First Search
Uses Queue	Uses Stack
Follows FIFO	Follows LIFO
Explores level by level	Explores depth-wise
Finds shortest path for equal-cost moves	Does not guarantee shortest path


37. What is a state transition?
A state transition means moving from one state to another by performing a valid action.
  
38. What is a state space?
State space is the collection of all possible arrangements of disks on the three rods.
  
39. What is the time complexity of BFS?
O(V + E), where V is the number of states and E is the number of transitions.
  
40. Why do we maintain a visited list?
To prevent repeated states and avoid unnecessary searching.

4. Tower of Hanoi Logic-Based Questions

41. What is the smallest disk?
Disk 1 is the smallest disk.

42. What is the largest disk?
Disk 3 is the largest disk.

43. Why do we use [-1]?
In Python, index -1 accesses the last element of a list or tuple. Here, it represents the top disk.

44. Can we move a larger disk onto a smaller disk?
No. It violates the rules of Tower of Hanoi.

45. Can we move more than one disk at a time?
No. Only one disk can be moved at a time.
  
46. What happens if the source rod is empty?
The program skips that movement because there is no disk available to move.
  
47. What is the auxiliary rod?
The auxiliary rod is the extra rod used temporarily while transferring disks from the source to the destination.

48. What is the minimum number of moves required for 3 disks?
The minimum number of moves is:
\[
2^n-1
\]
For 3 disks:
\[
2^3-1=7
\]
Therefore, the minimum is 7 moves.
