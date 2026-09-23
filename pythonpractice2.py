# -------------------- Section A: Loops ----------------------
# 1. Write a loop that prints the numbers from 1 to 10.
for number in range (1,11):
    print(number)

print()
# 2. Write a loop that prints only the even numbers from 1 to 20.

for number in range (1,21):
    if number % 2 == 0:
        print(number)
print()

# 3. Write a loop that calculates the sum of numbers from 1 to 100.
sum = 0

for number in range (1,101):
    sum += number
print(sum)

print()
# 4. Write a loop that prints each character of the word "Python" on its own line.

letters = 'Python'

for letter in letters:
    print(letter)

print()

# 5. Write a loop that prints a multiplication table for the number 5 (5 x 1 to 5 x 10).

for number in range(1,11):
    result = 5 * number

    print(f"5 * {number} = {result}")

print()

# 6. Write a loop that counts down from 10 to 1, then prints "Liftoff!".

for number in range (10,0,-1):
    print(number)

print("Liftoff!")  
print()

# 7. Write a loop using while that keeps asking a user to guess a number (hardcode the number as 7) until they get it right.

#Alternative one
secret_number = 7

guess = int(input("Guess a number: "))

while guess != secret_number:
    print('Number is incorrect')

    guess = int(input("Guess a number: "))

print('Correct!!')

# #Alternative two
secret_number = 7

guess = int(input("Guess a number: "))

while not guess == secret_number:
    print('Number is incorrect')
    
    guess = int(input("Guess a number: "))
    
print('Correct!!')

# ------------------------------------- Section B: Functions ------------------------------------

# 8. Write a function factorial(n) that returns the factorial of a number using a loop.

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result

print(factorial(9))
print()

# 9. Write a function is_leap_year(year) that returns True if the year is a leap year, False otherwise.

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

print(is_leap_year(2020))
print(is_leap_year(2022))
print(is_leap_year(1978))
print(is_leap_year(2008))
print()

# 10. Write a function sum_list(numbers) that takes a list of numbers and returns their sum, using a loop (not the built-in sum()).

def sum_list(numbers):
    total = 0

    for number in numbers:
        total += number
    return total
print(sum_list([1, 86, 4, 789, 25]))
print()       

# 11. Write a function reverse_string(text) that returns the reversed version of a string, using a loop (not slicing).

def reverse_string(text):
    reversed_text = ""

    for character in text:
        reversed_text = character + reversed_text
        # We're putting the new character in front of what we already have.
        # P + "" = P
        # y + "P" = yP
        # t + "yP" = tyP etc.
    return reversed_text
print(reverse_string("Python"))
print()

# 12. Write a function count_down(n) that prints numbers from n down to 1 using a loop inside the function.

def count_down(n):
    for i in range(n, 0, -1):
        print(i)

(count_down(7))
print()

# 13. Write a function average(numbers) that takes a list of numbers and returns their average.
def average(numbers):
    total = 0
    for number in numbers:
        total += number
        avg = total / len(numbers)
    return avg    
print(average([5, 10, 15]))
print()

# ---------------------- Section C: Data Structures ------------------------

# 14. Given the list ages = [23, 45, 12, 67, 34, 8], write a loop to print only the ages that are 18 or older.

#Alternative One
ages = [23, 45, 12, 67, 34, 8]

for age in ages:
    if age >= 18:
        print(age)
print()

#Alternative two

ages = [23, 45, 12, 67, 34, 8]

plus_50 = [age for age in ages if age >= 18]
print(plus_50)

print()

# 15. Given the dictionary prices = {"bread": 60, "milk": 55, "eggs": 15}, write a loop to print each item with its price formatted 
# as: "bread costs 60".

prices = {"bread": 60, "milk": 55, "eggs": 15}

for key, value in prices.items():
    print(f"{key} costs {value}")

print()

# 16. Given the list numbers = [10, 25, 3, 47, 8], write a loop that finds and prints the smallest number.

numbers = [10, 25, 3, 47, 8]

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number
print(smallest)

print()

# 17. Write code that builds a list of the squares of numbers from 1 to 10 using a loop (not a list comprehension).

squares  = []

for number in range (1,11):
    square = number * number
    squares.append(square)

print(squares)

# ---------------------------------------- Section D: Combining Loops, Functions & Data Structures -------------------------------------

# 18. Write a function count_occurrences(items) that takes a list and returns a dictionary showing how many times each item appears.
#  Example: count_occurrences(["a", "b", "a", "c", "b", "a"]) → {"a": 3, "b": 2, "c": 1}.

def count_occurrences(items):
    count = {}
    for item in items:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    return count
print(count_occurrences(["a", "b", "a", "c", "b", "a"]))
print()

# 19. Write a function filter_passed(scores) that takes a dictionary of {name: score} and returns a list of names who scored 50 or above.

def filter_passed(scores):
    passed = []

    for name in scores: # Goes through the keys in the dictionary
        if scores[name] >= 50:
            passed.append(name)

    return passed

print(filter_passed({"Amina": 70, "John": 45, "Mary": 80}))
print()

# 20. Write a function print_table(rows) that takes a list of lists (like a table) and prints each row on its own line, 
# with the values separated by " | ". Example: print_table([["Name", "Age"], ["Amina", 20], ["John", 22]]).

def print_table(rows):
    for row in rows:
        print(" | ".join(str(value) for value in row))

print_table([["Name", "Age"], ["Amina", 20], ["John", 22]])


