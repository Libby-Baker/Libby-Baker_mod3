# MCON 141 — Homework 3
# Class 3 Concepts: if statements and Boolean logic
#
# Name: Libby Baker
# Date: September 22, 2026
#
# DIRECTIONS
# 1. Open this file in Pyzo and save it with your own name in the filename.
# 2. Type your solution directly below each exercise's comment block.
# 3. For every exercise that asks for user input, place the input/conversion
#    statements in a try / except ValueError block.
# 4. Test every solution. If you do not use a function, leave comments stating
#    the additional tests you ran, because only the final run is visible.
# 5. All code must run without errors.
#
# EXTRA CREDIT (up to 2 points)
# Write your solutions inside functions where appropriate. For example:
#
# def check_weather(temperature):
#     if temperature > 80:
#         return "It is hot outside."
#     elif temperature < 60:
#         return "It is cold outside."
#     else:
#         return "The weather is mild."
#
# print(check_weather(75))  # should print: The weather is mild.
# print(check_weather(85))  # should print: It is hot outside.
# print(check_weather(50))  # should print: It is cold outside.


# ================================================================
# Exercise 1: What is x relative to y?
#
# Two variables are named x and y. Set y to 10 and x to 20.
#
# Write an if / elif / else statement that compares x and y:
# - If x is less than y, print: "x is less than y"
# - If x is equal to y, print: "x is equal to y"
# - If x is greater than y, print: "x is greater than y"
#
# In a comment within your code, explain the result and why it occurs.
# Also test at least two other values of x and/or y, and document those tests.

x = 20
y = 10

def compare():
    if x<y:
        print("x is less than y")
    elif x==y:
        print("x is equal to y")
    else:
        print("x is greater than y")
    # Function will print "x is greater than y, because both x<y & x==y are false. That leaves the last option. I also tested x valued at 5 (printed "x is less than y") and at 10 (printed "x is equal to y")

compare()




# ================================================================
# Exercise 2: Is x odd or even?
#
# Use x = 20 (or define x again so this exercise runs independently).
#
# If x is even, print: "x is even"
# Otherwise, print: "x is odd"
#
# In a comment within your code, explain the result and why it occurs.
# Test at least one odd value as well.

x = 21

def is_even():
    if x%2==0:
        print("x is even")
    else:
        print("x is odd")
    # Used mod. When an even number is divided by two, it leaves no remainder. So when x is twenty, it will print "x is even"

is_even()
# ================================================================
# Exercise 3: Polynomials
#
# Two factors, when multiplied together, can produce a binomial.
# Given (x + a) * (x + b), where a and b are integers:
#
#      x + a
#  *   x + b
# -------------
#        xb + ab
#   x^2 + xa
# -------------
#   x^2 + (xb + xa) + ab
#
# Write a program named polynomial that asks the user for integers a and b,
# then computes and prints the expanded binomial.
#
# Example: (x + 2) * (x + 3) = x^2 + 5x + 6
#
# Remember: x^2 means "x squared."
# Use try / except ValueError for user input.

def polynomial():
  a = input("Please enter a value for a").strip()
  b = input("Please enter a value for b").strip()

  try:
     a = int(a)
     b = int(b)

  except ValueError:
    print("Invalid input detected. Please enter an integer.")

  else:
    print(f"(x + {a})(x + {b})")
    mid_term = a+b
    end_term = a*b

    print(f"x^2 + {mid_term}x + {end_term}")



polynomial()
'''tested with negetive numbers (which worked fine for this and all of the following exercises), strings, floats (which triggered a ValueEerror here and in all subsequent exercises'''



# ================================================================
# Exercise 4: Analyze the polynomial
#
# Given integers a and b, expand (x + a)(x + b) into:
# x^2 + (xb + xa) + ab
#
# Then determine whether:
# - the middle-term coefficient (a + b) is positive, negative, or zero; and
# - the constant (a * b) is positive, negative, or zero.
#
# You may reuse your values of a and b from Exercise 3, but make this exercise
# run independently if possible. Use try / except ValueError for user input.

def analyze_polynomial():
  a = input("Please enter a value for a").strip()
  b = input("Please enter a value for b").strip()

  try:
     a = int(a)
     b = int(b)

  except ValueError:
    print("Invalid input detected. Please enter an integer.")

  else:
    print(f"(x + {a})(x + {b})")
    mid_term = a+b
    end_term = a*b

    print(f"x^2 + {mid_term}x + {end_term}")

    if mid_term > 0:
      print("Middle-term coefficient is positive.")
    elif mid_term < 0:
      print("Middle-term coefficient is negetive")
    else:
      print("Middle-term coefficient is 0")

    if end_term > 0:
      print("Constant is positive.")
    elif end_term < 0:
      print("Constant is negetive")
    else:
      print("Constant is 0")

analyze_polynomial()
'''tested with negetive numbers, letters, and floats'''




# ================================================================
# Exercise 5: Explore the and statement
#
# Ask the user to enter integers val1 and val2.
#
# - If both values are positive, print: "val1 and val2 are positive"
#   and print the values.
# - If both values are negative, print: "val1 and val2 are negative"
#   and print the values.
# - Otherwise, print: "The values are not both positive or both negative"
#   and print the values.
#
# Use try / except ValueError for user input.

val1 = (input("Enter the first value"))
val2 = (input("Enter the sencond value"))

try:
  val1 = int(val1)
  val2 = int(val2)

except ValueError:
    print("not a valid value")


else:
  if val1 > 0 and val2 > 0:
    print("val1 and val2 are positive")

  elif val1 < 0 and val2 < 0:
    print("val1 and val2 are negetive")

  else:
    print("The values are neither both positive nor both negetive")

  print(f"val1: {val1}",f"val2: {val2}")
  '''tested with positive numbers, negetive numbers, strings, floats'''



# ================================================================
# Exercise 6: Explore the or statement
#
# Ask the user to enter integers val1 and val2.
#
# - If val1 or val2 is positive, print: "At least one value is positive"
#   and print the values.
# - If val1 or val2 is equal to zero, print: "At least one value is zero"
#   and print the values.
# - Otherwise, print: "At least one value is negative"
#
# Use try / except ValueError for user input.

val1 = (input("Enter the first value"))
val2 = (input("Enter the second value"))

try:
  val1 = int(val1)
  val2 = int(val2)

except ValueError:
   print("Invalid input detected. Please enter integer")


else:
  if val1 > 0  or val2 > 0:
    print("At least one value is positive")

  if val1 == 0 or val2 == 0:
    print("At least one value is equal to zero")

  else:
    print("At least one of these values are negetive")

  print(f"val1: {val1}",f"val2: {val2}")
  '''tested with positive numbers, negetive numbers, strings, and floats'''


# ================================================================
# Exercise 7: Explore not
#
# Set the following variables:
# a = True
# b = True
# c = False
#
# Evaluate and print the results of these expressions:
# 1. not (a and b)
# 2. not a or not c
# 3. not ((a and c) and b)
#
# Include a comment explaining each result.

a = True
b = True
c = False

print(not(a and b))# flips a to flase and b to false, since at least one is false, it prints false
print(not(a) or not(c))# flips a to false and c to true. Since at least one is true, prints true
print(not((a and c) and b))#a and c would be false, add b, all is false, the whole things flips true



# ================================================================
# Exercise 8: Voting Age and Citizenship
#
# Ask the user for their age and whether they are a citizen (yes or no).
#
# - If they are 18 or older AND a citizen, print:
#   "You are eligible to vote."
# - If they are under 18 OR not a citizen, print:
#   "You are not eligible to vote."
#
# Hint: use and for the eligibility requirements. Use try / except ValueError
# for the age input.

def voting():
  age = input("How old are you? ")
  '''
  try/except will convert the input unless the input is not convertable (ie. not an integer)
  '''
  try:
    age = int(age)

  except ValueError:
    print("Invalid age input, please enter an integer")

  else:#once we've safely converted the age to an integer, we can collect the other piece of data and analize it
    citi = input("Are you a citizen yes/no").strip().lower()

    if age >= 18 and citi == "yes":
      print("you are eligable to vote")
    if age < 18 or citi =="not":
        print("you are not eligeable to vote")

voting()

'''age was tested with strings, floats'''

# ================================================================
# Exercise 9: Number Classification
#
# Ask the user for an integer.
#
# - If it is positive and even, print: "Positive even number."
# - If it is positive and odd, print: "Positive odd number."
# - If it is negative or zero, print: "Not a positive number."
#
# Hint: combine and and or. Use try / except ValueError for user input.

num = input("Please enter an integer")#sets num as input

try:
  num = int(num)#converts string input to integer if possible

  if num > 0 and num%2 == 0:
    print("Positive even number")
  if num > 0 and num%2 == 1:
    print("Positive odd number")
  if num < 0 or num == 0:
    print("Not a positive number")

except ValueError:
   print("This is not a valid input")#if input can't be converted to integer, sends value error message

'''tested with strings, floats, positive numbers and negetive numbers'''

# ================================================================
# Exercise 10: Triangle Check
#
# Ask the user for three side lengths: a, b, and c.
#
# Print "Valid triangle." only if all sides are greater than 0 AND:
# - a + b > c
# - a + c > b
# - b + c > a
#
# Otherwise, print "Not a valid triangle."
#
# Hint: chain multiple and conditions. Use try / except ValueError for input.

def triangle_check():
  a,b,c = input("Enter integer for side a "), input("Enter integer for side b "), input("Enter integer for side c ")
  try:
    a_int, b_int, c_int = int(a), int(b), int(c)
    if a_int + b_int > c_int and a_int + c_int > b_int and b_int + c_int > a_int:
      print("Valid triangle")
    else:
      print("Not a valid triangle")
  except ValueError:
    print("Invalid input detected. Please enter an integer")

triangle_check()

'''tested with strings, floats, positive numbers and negetive numbers'''

# ================================================================
# Exercise 11: Weekend Plan Decision Tree
#
# Ask the user two questions:
# - Is it the weekend? (yes or no)
# - Do you have homework? (yes or no)
#
# Build a decision tree that prints:
# - Weekend and no homework: "Go have fun!"
# - Weekend and homework: "Do your homework first, then relax."
# - Not weekend and homework: "Focus on schoolwork."
# - Not weekend and no homework: "It's a regular day, keep learning!"
#
# Consider converting responses to lowercase so Yes, YES, and yes all work.

def decision_tree():
  weekend = input("Is it a weekend? (yes/no)").strip().lower()
  hw = input("Do you have homework? (yes/no)").strip().lower()

  if weekend == "yes" and hw == "no":
    print("Go have fun!")
  elif weekend == "yes" and hw == "yes":
    print("Do your homework first, then relax.")
  elif weekend == "no" and hw == "yes":
    print("Focus on schoolwork.")
  else:
    print("It's a regular day, keep learning!")

decision_tree()
