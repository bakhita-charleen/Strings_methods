# Section A: Functions 
# 1. Write a function greet(name) that returns "Hello, <name>!".

def greet(name):
    print(f"Hello, {name}!")

greet('Charleen')
print()

# 2. Write a function add(a, b) that returns the sum of two numbers.

def add (a,b):
    return (a + b)

print(add(5,6))
print()

# 3. Write a function is_even(n) that returns True if a number is even, False if odd.
def is_even(n):

    if n % 2 ==0:
        print('True')
    else:
        print('False')

is_even(66) 
print()       

# Another alternative

def is_even(n):
    return n % 2 == 0

print(is_even(6))
print(is_even(7))
print()

# 4. Write a function square(n) that returns the square of a number. Then use it to print the squares of 1 to 5.

def square(n):
    return n ** 2

print(square(5))
print()

#Alternative
def square(n):
    return n ** 2

result = square(9)
print(result)
print()

# 5. Write a function max_of_two(a, b) that returns the larger of two numbers (without using the built-in max()).
def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b
print(max_of_two(9, 7)) 
print()   

# Section B: Data Structures 
# 6. Given the list fruits = ["apple", "banana", "cherry"],
#  write code to add "mango" to the end, 
# then print the full list.

fruits = ["apple", "banana", "cherry"]
fruits.append('mango')
print(fruits)
print()

# 7. Given the list numbers = [5, 12, 8, 3, 20],
#  write code to find and print the largest number
#  using a loop.

numbers = [5, 12, 8, 3, 20]

largest = 0

for number in numbers:
    if number > largest:
        largest = number

print(f"Largest number is: {largest}")
print()

# 8. Create a dictionary 
# student = {"name": "Amina", "age": 20, "course": "Data Science"}.
#  Write code to print each key and value on its own line.

student = {"name": "Amina", "age": 20, "course": "Data Science"}

for key, value in student.items():
    print(f"{key}: {value}")

print()

# 9. Given the list numbers = [1, 2, 3, 4, 5, 6],
#  write code to print only the even numbers.

numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    if number % 2 ==0:
        print(number)
print()  

# 10. Write code that counts how many times the number 3 
# appears in the list [3, 5, 3, 2, 3, 8].

numbers = [3, 5, 3, 2, 3, 8]

print(numbers.count(3))
print()

#Alternative two

numbers = [3, 5, 3, 2, 3, 8]

count = 0

for number in numbers:
    if number == 3:
        count += 1
print(count)
print()

# ---------------------------- Section C: String Methods -----------------------------------

# 11. Given the string text = "  Hello World  ", write code to remove the extra spaces and convert it to all lowercase.

text = "  Hello World  "
print(text)

new_text = text.strip().lower()
print(new_text)
print()

# 12. Write a function count_letter(word, letter) that counts how many times a specific letter appears in a word.
#  Example: count_letter("banana", "a") → 3.

def count_letter(word, letter):
    return word.count(letter)  # Count the letter and return the result

print(count_letter('banana', 'a'))
print()

# --------------------------------------------- Section D: ----------------------------------------------------------
# 13. Write a function count_words(sentence) that takes a sentence and returns how many words are in it (hint: use .split()).

def count_words(sentence):
    words = len(sentence.split())
    return words
 
print(count_words("I will be a billionaire"))
print()

# 14. Write a function longest_word(sentence) that takes a sentence and returns the longest word in it.

def longest_word(sentence):
    words = sentence.split()
    longest = words[0] # assuming the word on index 0 which is 'I' is the longest

    for word in words: 
        if len(word) > len(longest):
            longest = word
    return longest

print(longest_word("I will become a billionaire"))
print()

# 15. Write a function make_initials(full_name) that takes a name like "John Kamau" and returns "J.K." 
# (hint: split the name, take the first letter of each part).

def make_initials(full_name):
    parts = full_name.split()
    initials = ""

    for part in parts:
        initials += part[0].upper() + "."

    return initials
print(make_initials('Kylie Kristen Jenner'))

