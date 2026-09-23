'''
Topic 8: Prefixes, suffix and professional formatting
'''

# Example 1: Startswith() and endswith()
phone = "0712345678"

print(phone.startswith('07'))
print(phone.startswith('01'))
print(phone.endswith('678'))
print()

filename = "report.pdf"
print(filename.endswith('.pdf'))
print(filename.endswith('.docx'))
print()

#Checking a file's TYPE by its ending before trying to open it

#Example 2: Profession formatting
# {value:<width} left align
# {value:> width} right align

products = [
    ("Laptop", 85000),
    ("Phone", 45000),
    ("Headphones", 3500),
    ("Monitor", 22000)
]

print(f"{'Product':<15} {'Price':>12}")
print('-' * 30)
for product, price in products:
    print(f"{product:<15} Ksh {price:>8}")
print()

name = 'Charleen'

print(f"[{name:<10}]") #left align, pad to 10 characters
print(f"[{name:>10}]") #right align,pad to 10 characters
print(f"[{name:^10}]") #centre-align, pad to 10 characters
print()

#Example 3: Controlling the decimals
price = 349.6789 #KES 349.68
print(f"KES {price:.2f}")
print()

average = 76.3333333  # Average: 76.3
print(f"Average: {average:.1f}")
print()


'''
Topic 9: Reading from a file
'''

# Example: Opening and closing a file

'''
Syntax: 
    open(filename, mode) 
'''
my_file = open("notes.txt", "w")
my_file.write("Hello, this is my first file")
my_file.close()

# The with Statement (best practice)
with open("notes.txt", "w") as my_file:
    my_file.write("Hello again, but safer this time")

#Example 1: read()- everything at once
with open('students.txt', 'r') as f:
    c = f.read()
print(c)
print(type(c))
print()

with open ('students.text', 'r') as f:
    for line in f:
        print(line.strip())
print()

#Example 3: read all lines into a list
with open('students.txt', 'r') as f:
    lines = f.readlines()

print(lines)
print(f"Total Students: {len(lines)}")


# with open('students.txt', 'r') as f:
#     first_line = f.readline()
#     second_line = f.readline()

# Create a text file called routes.txt (you can do this from VS Code) with 4 matatu route names, one per line.
# Write code to open the file and print each route, cleaned with .strip(), using the for line in file: pattern.
# Separately, open the same file with readlines() and print the total number of routes using len().

