# Question 1 - Slicing a Town Name

# Create a variable called town with the value 'Mombasa'.
# Print the first 3 letters using slicing.
# Print the last 2 letters using slicing.
# Print the whole word reversed using [::-1].

town = 'Mombasa'

# Print the first 3 letters using slicing.
print(town[0:3])
# Print the last 2 letters using slicing.
print(town[-2:])
# Print the whole word reversed using [::-1].
print(town[::-1])

print()

# Question 2 - Building Initials

# Create a variable called full_name with the value 'Amina Wanjiku'.
# Using indexing and slicing (NOT split, save that for later),
# extract the first letter of the first name and the first letter of the last name.
# Print the initials as 'A.W.'

full_name = 'Amina Wanjiku'

first_initial = full_name[0]
last_initial = full_name[6]

print(f"{first_initial}.{last_initial}")
print()

#Question 3
# Create a variable called raw_name with the value 'bRIAN oTIENO'.
# Print it fixed so it reads 'Brian Otieno' using the correct method.
# Separately, print raw_name using swapcase() just to see the result.
# Print raw_name using capitalize() and explain in a comment why the result looks different from title().

raw_name = 'bRIAN oTIENO'

print(raw_name.title())
print(raw_name.swapcase())
print(raw_name.capitalize())
print()

#Question 4
# Create a variable called code with the value '###PROMO2024###'.
# Use strip('#') to remove just the hash symbols, and print the result.
# Create a second variable messy_price with the value '   450   '.
# Clean it with strip(), then convert it to an integer using int(), and print it plus 50.

code = '###PROMO2024###'
print(code.strip('#'))

messy_price = '   450   '
price = int(messy_price.strip())
print(price + 50)
print()

# Section D - Splitting & Joining
#Question 5
# Create a variable called record with the value 'Njeri,88,Kisumu'.
# Split it by the comma into a list called fields.
# Print each field separately with a label, e.g. 'Name: Njeri', 'Score: 88', 'Town: Kisumu'.
record = 'Njeri,88,Kisumu'

fields = record.split(',')

print(f" Name: {fields[0]}")
print(f" Score: {fields[1]}")
print(f" Town: {fields[2]}")
print()

# Question 6 - Building a Shopping Sentence

# Create a list called items with 4 grocery items of your choice.
# Use join() to combine them into one sentence separated by ', ', but make the LAST item joined with ' and ' instead.
# Expected style: 'Bread, Milk, Sugar and Rice'
# Hint: join everything except the last item first, then add ' and ' plus the last item.

items = ['Oats', 'Cornflakes', 'Wheat', 'Candy']

result = ', '.join(items[:3]) + ' and ' + items[3]

print(result)


# Section E - Searching & Replacing
# Question 7 - M-Pesa Message Checker

# Create a variable called sms with the value 'Confirmed. You have received KES 2500 from JOHN KAMAU on 24/08/26'.
# Use in to check if 'received' is in the message, and print the result.
# Use .find() to get the position of the word 'KES' in the message.
# Use .find() to search for the word 'sent' - print the result and explain in a comment what the -1 means.

sms = 'Confirmed. You have received KES 2500 from JOHN KAMAU on 24/08/26'

print('received' in sms) #returns true - Received is present
print(sms.find('KES')) # returns 29 - position of the 'KES
print(sms.find('sent')) # returns -1 - sent not found
print()

# Question 8 - Censoring a Word

# Create a variable called comment with the value 'This matatu is too slow, the driver is careless'.
# Use .count() to count how many times the letter 's' appears.
# Use .replace() to swap the word 'careless' for 'reckless', and print the new sentence.
# Use .replace() again to censor the word 'slow' by replacing it with '****', and print the final result.

comment = 'This matatu is too slow, the driver is careless'
print(comment)

print(comment.count('s'))

new_comment = comment.replace('careless', 'reckless')
print(new_comment)

another_comment = comment.replace('slow', '****')
print(another_comment)
print()

# Section F - Validating Text
# Questions 9–10
# Question 9 - PIN Validator

# Write code that keeps asking the user 'Enter a 4-digit PIN: '
#  in a loop, until they type something where .isdigit() 
# is True AND the length is exactly 4.
# Once valid, print 'PIN accepted.'
# Test it by first typing something invalid (letters, or the wrong length), then a valid PIN.

pin = input('Enter a 4-digit PIN: ')

while not pin.isdigit() or len(pin) != 4: #is it digits only and is it 4 characters long
    print("Invalid PIN. Please try again.")
    pin = input("Enter a 4-digit PIN: ")

print("PIN accepted.")
print()

# Question 10 - Classify the Input

# Create a list called samples with these 5 values: ['Amina', '12345', 'Amina123', '   ', 'AMINA']
# Loop through the list. 
# For each item, print the item and check/report 
# ALL of the following: is it alpha, is it a digit,
#  is it alnum, is it upper.
# Format: 'Amina - alpha: True, digit: False,
#  alnum: True, upper: False'

samples = ['Amina', '12345', 'Amina123', '   ', 'AMINA']

for item in samples:
    print(f"{item} - alpha: {item.isalpha()}, digit: {item.isdigit()}, alnum: {item.isalnum()}, upper: {item.isupper()}"
           )
    print()

# Question 11 - Payslip Formatter
 
# Create variables: salary = 85000, deduction = 4500, and net_pay = salary - deduction.
# Print all 3 values with a thousands separator and a 'KES' prefix, e.g. 'Net Pay: KES 80,500'.
# Create a variable receipt_no = 42 and print it zero-padded to 5 digits, e.g. 'Receipt #00042'.
 
salary = 85000
deduction =4500
net_pay = salary - deduction
print(f"Salary: KES {salary:,}")
print(f"Deduction: KES {deduction:,}")
print(f"Net Pay: KES {net_pay:,}")
receipt_no = 42
print(f"Receipt #{receipt_no:05d}") 
                            #d means treat it as an integer
                            # 5 means make ot 5 digits/ characters long/wide
                            # 0 means fill the empty spaces with 0
# print("Receipt #" + str(receipt_no).zfill(5))
                        #str(receipt_no) - converts it to a string
                        # .zfill(5) - make it 5 character wide
print()

'''
Question 12 - Aligned Mini Report
 
Create a list of tuples: sales = [('Bread', 650), ('Milk', 840), ('Sugar', 750)]
Loop through the list and print each item name left-aligned to 12 characters, followed by the amount right-aligned to 8 characters with a thousands separator.
Expected style: 'Bread       KES     650'
'''

sales = [('Bread', 650), ('Milk', 840), ('Sugar', 750)]
# Each item is a tuple containing: (item name, amount)
# step 1: loop throgh the list of tuples
for item, amount in sales:
    # step 2: print the item name left-aligned to 12 characters,
    # and amount right-aligned to 8 characters with thousands separator
    print(f"{item:<12} KES {amount:>8,}")

