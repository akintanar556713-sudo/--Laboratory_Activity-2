# Explain the overall design of your program and justify why you chose this particular class structure and set of user-defined methods.
# 1 The program uses an Object-Oriented design to encapsulate student data, employing specific methods to ensure data validation (preventing invalid scores) and logic abstraction (centralizing the pass/fail criteria) for better maintainability.

# Describe how user input is handled in your program and discuss the role of exception handling (try–except) in preventing incorrect or unexpected behavior.
# 2 The program captures user input via the input() function and converts it to floats for numerical processing, using a try except block to act as a safety net that catches ValueErrors (like entering text instead of a number) or custom range violations, ensuring the script terminates gracefully with a helpful message rather than crashing.

# Identify one limitation of your current implementation and explain how it could be improved using additional OOP concepts or better error handling.
# 3 One significant limitation is that the input loop lacks persistence; if a user enters an invalid score or non-numeric text, the program catches the error but immediately terminates. To improve this, you could implement recursive error handling or a while loop within a method to repeatedly prompt the user until valid data is received, ensuring the program doesn't exit prematurely.
