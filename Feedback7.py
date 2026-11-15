
# Intelligent Number Guessing Agent

# Hidden number 
number = 75

# Set range
low = 1
high = 100

# Guess the number
while low <= high:

    # Calculate middle value
    guess = (low + high) // 2

    print("Agent Guess:", guess)

    # Check the guess
    if guess == number:
        print("Correct Guess!")
        break

    elif guess < number:
        print("Higher")
        low = guess + 1

    else:
        print("Lower")
        high = guess - 1


# Aim
# To design an intelligent agent that guesses a hidden number using higher/lower feedback in Python.

# Objectives
# 1. To understand the working of an intelligent agent.
# 2. To guess a hidden number within a given range.
# 3. To use feedback to improve the next guess.
# 4. To find the correct number using minimum guesses.

# Theory
# A number-guessing intelligent agent is an agent that guesses a hidden number based on feedback received from the environment.
# If the guess is too low, the agent receives "Higher" feedback. If the guess is too high, it receives "Lower" feedback. The agent uses this information to adjust its range and make a better guess.
# This process continues until the correct number is guessed. The agent uses the Binary Search technique to find the number efficiently.

# Algorithm
# 1. Start the program.
# 2. Set the minimum and maximum number.
# 3. Select a hidden number.
# 4. Calculate the middle number as the agent's guess.
# 5. Compare the guess with the hidden number.
# 6. If the guess is correct, display "Correct Guess".
# 7. If the guess is low, increase the minimum value.
# 8. If the guess is high, decrease the maximum value.
# 9. Repeat until the correct number is guessed.
# 10. Stop the program.

# Conclusion
# Thus, we successfully designed an intelligent number-guessing agent using Python. The agent uses higher/lower feedback and the Binary Search technique to find the hidden number efficiently.



1. What is the aim of this program?
The aim is to find a hidden number between 1 and 100 using the Binary Search Algorithm.

2. Which algorithm is used in this program?
Binary Search Algorithm.

3. What is Binary Search?
Binary Search is a searching algorithm that repeatedly divides the search range into two halves to find the required element.

4. Why is this program called an Intelligent Number Guessing Agent?
Because the agent uses feedback from previous guesses to make better decisions and reach the correct answer.
  
5. What is an AI Agent?
An AI Agent is an entity that observes its environment and takes actions to achieve a specific goal.

6. What is the goal of this agent?
To find the hidden number 75 using the minimum possible guesses.

7. What is the initial range?
The initial range is from 1 to 100.

8. What is the hidden number?
The hidden number is 75.

9. How does the agent decide its next guess?
It calculates the middle value of the current search range.
  
10. What are the three possible results of a guess?
- Correct Guess
- Higher
- Lower

2. Python Code-Based Viva Questions

11. What is the use of while loop?
It repeatedly executes the guessing process until the correct number is found or the search range becomes invalid.

12. What is the use of low?
It represents the lower limit of the current search range.

13. What is the use of high?
It represents the upper limit of the current search range.

14. What is the use of guess?
It stores the current number guessed by the agent.
  
15. What is the use of // operator?
It performs floor division and returns the integer quotient.
Example:
75 // 2 = 37

16. Why do we use (low + high) // 2?
To calculate the middle value of the current search range.

17. What is the use of if?
It checks whether the guessed number is equal to the hidden number.

18. What is the use of elif?
It checks whether the guessed number is smaller than the hidden number.

19. What is the use of else?
It executes when the guessed number is greater than the hidden number.

20. What is the use of break?
It immediately terminates the loop when the correct number is found.

21. Why do we use low = guess + 1?
When the guess is smaller than the hidden number, all numbers up to the current guess are eliminated.
  
22. Why do we use high = guess - 1?
When the guess is greater than the hidden number, all numbers from the current guess onwards are eliminated.
  
3. Important Binary Search Questions
These are particularly important for your AI viva.
                                
23. How does Binary Search work?
Binary Search works in the following steps:
1. Set the initial range from 1 to 100.
2. Calculate the middle value.
3. Compare the middle value with the hidden number.
4. If equal, the number is found.
5. If smaller, search the upper half.
6. If greater, search the lower half.
7. Repeat until the number is found.

24. What is the time complexity of Binary Search?
The time complexity is O(log n).

25. What is the space complexity of this program?
The space complexity is O(1) because it uses only a fixed number of variables.

26. What is the difference between Linear Search and Binary Search?
Linear Search	Binary Search
Checks elements one by one.	Divides the range into halves.
Time complexity O(n).	Time complexity O(log n).
Can work on unsorted data.	Requires sorted data or an ordered search range.
Generally slower.	Generally faster.


27. Why is Binary Search faster than Linear Search?
Because Binary Search eliminates approximately half of the remaining search range after every guess.

28. Does Binary Search require sorted data?
Yes, Binary Search requires sorted data or an ordered search space.
  
29. What happens if the guessed number is correct?
The program prints "Correct Guess!" and stops the loop using break.

30. What happens if the hidden number is greater than the guess?
The program prints "Higher" and increases the lower limit.
  
31. What happens if the hidden number is smaller than the guess?
The program prints "Lower" and decreases the upper limit.
  
32. What happens if the number is not found?
The loop terminates when low becomes greater than high.

4. AI-Based Conceptual Viva Questions

33. What type of agent is used in this program?
It can be considered a simple goal-based agent because it takes decisions to achieve the goal of finding the hidden number.

34. What is the environment in this program?
The environment is the number range between 1 and 100.

35. What are the actions performed by the agent?
The agent guesses a number and updates the search range based on feedback.

36. What is the goal state?
The goal state is finding the hidden number 75.

37. Is this a searching problem?
Yes, it is a searching problem because the agent searches for a specific number within a given range.

38. Does this program use Machine Learning?
No. It uses a predefined Binary Search algorithm and does not learn from training data.

39. What is the advantage of this program?
It finds the hidden number efficiently by reducing the search range by half after every guess.

5. Output-Based Viva Questions

40. What is the output of this program?
The hidden number is 75.
The agent performs the following guesses:
Agent Guess: 50
Higher
Agent Guess: 75
Correct Guess!

41. How many guesses are required to find 75?
Only 2 guesses.

42. Why does the agent first guess 50?
Because 50 is the middle value of the initial range from 1 to 100.

43. Why does the agent guess 75 next?
Because the first guess was smaller than the hidden number, so the agent updates the lower limit to 51. The middle of 51 and 100 is 75.

44. What is the maximum number of guesses required for a range of 100 numbers?
At most 7 guesses.
