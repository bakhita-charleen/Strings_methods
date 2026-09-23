#-------------------------- Topic 1: Strings are sequences ----------------------------

'''
String is just a list of characters

'Nairobi' behaves like ['N', 'a', 'i', 'r', 'o', 'b', 'i']
    position 0 is 'N', -1 is 'i'

'''

city = 'Nairobi'
print(city[0])
print(city[-1])
print(len(city))

print()

# Example 2: Slicing a string
city = 'Nairobi'
print(city[0:3])        #Nai
print(city[3:])         #robi
print(city[::-1])       #Iborian

print()

# Example 3: Concatenation(+) and repetition (*)
first = 'Nai'
second = 'robi'

print(first + second)
print("ha" * 3)
print('-' * 20)

city2 = 'Kisumu'
city2 = 'N' + city2[1:]
print(city2)
print()
'''
Topic 2: Changing case

'Nairobi' == 'nairobi'  --> False, Python treats capital and lowercase as completely different characters

String methods lets you standardize text BEFORE comparing it.

    upper(), lower(), title(), capitalize()
'''

# Example 1:
name = "young odhiambo"
print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())
print()

# Example 2: Swapcase

shout = "Hello WORLD"
print(shout.swapcase())
print()

'''
Topic 3: Removing extra spaces

a user typing their name into input() might accidentally leave spaces: '  yes'
'yes' == '  yes  ' --> False. That inviisble whitespace breaks comparison

'''

# Example 1: strip(), lstrip(), rstrip()

name = '  Brian  '
print(len(name))
print(f"[{name.strip()}]")  # removes spaces from both sides.
print(f"[{name.lstrip()}]") # removes spaces from LEFT ONLY.
print(f"[{name.rstrip()}]") # removes spaces from RIGHT ONLY.
print()

# Example 2: strip(can remove characters)
code = "###PROMO2026###"

print(code.strip('#'))
print()

'''
Topic 4: Splitting text apart
split() breaks a string into a LIST of pieces, using a separator you choose
(a space by default)

'''

#Example 1: split() - with default separator
sentence = "Moses is learning python in Nairobi"
words = sentence.split()
print(words)
print(len(words))
print()

#Example 2: split() with custom separator
record = "Amina, 78, Nairobi"
fields = record.split(',')
print(fields)
print(fields[0])
print(fields[1])
print()

#Example 3: splitlines() - breaking multi-line text apart

notes = "Buy bread\nPay rent\nCall Mercy"
print(notes)
lines = notes.splitlines()
print(lines)
print()

'''
Topic 5: Putting text back together

.join() is the reverse of split()
syntax is: 
            separator.join(list) glues a list of strings together into ONE string.            
'''

#Split
csv_line = "Brian,24,Nairobi,Data Science"
fields = csv_line.split(',')
print(fields)

#Join
cities = ['Nairobi', 'Mombasa', 'Kisumu']
result = ' | '.join(cities)
print(result)

# clean csv and re-join
dirty = "   Brian   ,   24      ,       Nairobi     "
print(f"[{dirty}]")
print(f"[{dirty.strip()}]")

clean = dirty.split(',')
for p in clean:
    print(f"[{p}]")

clean = [i.strip() for i in dirty.split(',')]
clean_csv = " , ".join(clean)
print(f"[{clean_csv}]")
print()

# Example: join() with a newline
notes = ['Buy bread', 'Pay rent', 'Call Mercy']
file_content = '\n'.join(notes)

print(file_content)
print()

'''
Topic 6: Searching and replacing
- sometime you just need to know if something is there.
WHERE it is., HOW MANY times it appears , or you want to swap with something else
'''

# Example 1: The in operator - quick yes/no check

message = "Your M-Pesa transaction of KES 500 was successful"
print('M-Pesa' in message)
print('failed' in message)

# Example 2: find(), index() - WHERE is it?
message = "Your M-Pesa transaction of KES 500 was successful"
print(message.find('KES'))          #returns the position
print(message.find('failed'))       #returns -1 if not found - does not crash
print(message.index('KES'))         #also returns the position
print(message.index('failed'))      #this crashes

'''
use.find() when the text might NOT be thre
        - It safely returns -1 instead of crashing
use.index() only when you are CERTAIN the text exists, or otherwise crashes
'''

# Example 3: count() and replace()

text = 'banana'
print(text.count('a'))

message = "Your M-Pesa transaction of KES 500 was successful"
new_message = message.replace('successful', 'reversed')
print(new_message)

'''
Topic 7: checking what kind of TEXT it is

Every input() gives you back a STRING - even if user types a number
Before converting with int() its good practice to check the text
actually LOOKS like a number
'''

print("12345".isdigit())            #True
print("Amina".isdigit())            #False
print("Amina".isalpha())            #True
print("Amina123".isalnum())         #True
print("Amina 123".isalnum())        #False

# Example 2: Real use case

phone = input("Enter your phone number: ")

while not phone.isdigit():
    print("Please enter digits only")
    phone = input("Enter your phone number: ")

print(f"Thanks! Saved number: {phone}")