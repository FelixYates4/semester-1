'''# Worksheet 1.2: Task 1 Solution
## Task 1

Edit the file named `task1.py`. In this file, write a program that
* Asks users to enter an integer grade in the range 0 to 100
* Converts that grade into a result of Pass, Fail or Distinction, where

  - Fail = 0-39
  - Pass = 40-69
  - Distinction = 70-100

* Prints out the numeric grade and the result **on a single line**, with
  *exactly* same format as the examples below:

      82 is a Distinction
      57 is a Pass
      36 is a Fail

If the user enters something that isn't a number, or they enter an integer
value outside the required range, the program should immediately exit, after
first displaying this exact error message on the standard error channel:

    Error: Grade must be an integer between 0 and 100

Use the `exit()` function from Python's `sys` module to achieve this. Here
is an example of how you import this module and use the `exit()` function:

```python
import sys

sys.exit("Error!")
```

### Hints

Strings have an `isdecimal()` method that will tell you whether they could
be parsed as a decimal integer.'''

import sys

score = input("enter a number 0-100: ")

# Check if the input is a valid non-negative integer
if not score.isdecimal():
    sys.exit("Error: Grade must be an integer between 0 and 100")

score = int(score)

# Check if the score is within the allowed range (0 to 100)
if score < 0 or score > 100:
    sys.exit("Error: Grade must be an integer between 0 and 100")

# Determine the grade outcome
if score <= 39:
    grade = "Fail"
elif score <= 69:
    grade = "Pass"
else:
    grade = "Distinction"

# Print the result on a single line
print(f"{score} is a {grade}")