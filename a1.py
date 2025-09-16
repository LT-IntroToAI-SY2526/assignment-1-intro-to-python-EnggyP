# Assignment 1: AI-Generated Python Problems
# Name: [Enggy Puma]

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
[I'm learning Python basics in a high school programming class. I have don't have any experience with Python.
I'm new to programming. Can you create 5-7 practice problems that cover:
> - Data
> - Conditionals (if/elif/else)
> - Loops (for and while)
> - Functions
> - Basic list operations
> 
> Make them progressively more challenging. Make sure each problem has clear instructions and example inputs/outputs. Without having to print the code.]

Example: "I'm learning Python basics in a high school programming class. 
I have don't have experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: [Age In Months]
[ Write a function called age_in_months that takes in one number (a person's age in years) and returns how many months old they are.]

"""
def age_in_months(num):
    months = num * 12
    return months


"""

Example: 
Problem: Write a function called 'is_even' that takes an integer and returns 
True if the number is even, False if it's odd.

Example inputs/outputs:
- is_even(4) should return True
- is_even(7) should return False
"""
"""
PROBLEM 2: [Odd or Even?/Conditials (if/else)]
[Write a function called is_even that takes in a number and returns the string "Even" if it's even, or "Odd" if it's odd.]
"""

def check_number(num):
    if num % 2 == 0:
        return True
    else:
        return False
def is_even(num):
    return num % 2 == 0



"""
PROBLEM 3: [Count Down from a Number]
[ Write a function called count_down that takes a number and returns a list counting down to 0.]
"""
def count_down(start):
    return list(range(start, -1, -1))
    


"""
PROBLEM 4: [First Letter Checker]
[ Write a function called starts_with_a that takes a word and returns True if it starts with the letter 'a' or 'A', and False otherwise.]


"""

def starts_with_a(word):
    if len(word) == 0:
        return True
    first_letter = word[0]
    if first_letter == 'a' or first_letter == 'A':
        return True
    else: 
        return False



"""
PROBLEM 5: [FizzBuzz Life]
[ Write a function called fizzbuzz_lite that takes a number n and returns a list from 1 to n.
If a number is divisible by 3, put "Fizz" instead.


If it's divisible by 5, put "Buzz".


If divisible by both 3 and 5, put "FizzBuzz".]
"""
def fizzbuzz_lite(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result += ["FizzBuzz"]
        elif i % 3 == 0:
            result += ["Fizz"]
        elif i % 5 == 0:
            result += ["Buzz"]
        else:
            result += [i]
    return result



"""








# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================

"""
"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:

print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print(age_in_months(10))
print(age_in_months(5))

print(f"is_even(15): {is_even(15)}") 
print(f"is_even(20): {is_even(20)}") 


print(count_down(4))
print(count_down(7))

print(starts_with_a("apricot"))
print(starts_with_a("mango"))


print(fizzbuzz_lite(17))


