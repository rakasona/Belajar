# STRINGS
# Assign String to a Variable
import pickle as pc
import os
a = "Hello"
print(a)

# Multiline Strings
a = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""
print(a)

# Strings are Arrays
a = "Hello, World!"
print(a[1])

# String Length
a = "Hello, World!"
print(len(a))

# Check String
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

# Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

# String Manipulation in Python
# Creation
word = "Hello World"
print(word)

# Accessing
word = "Hello World"
letter = word[0]
print(letter)

# Length
word = "Hello World"
print(len(word))

# Finding
word = "Hello World"
print(word.count('l'))  # count how many times l is in the string
print(word.find("H"))  # find the word H in the string
print(word.index("World"))  # find the letters World in the string

# Count
s = "Count, the number of spaces"
print(s.count(' '))

# Slicing
word = "Hello World"

print(word[0])  # get one char of the word
print(word[0:1])  # get one char of the word (same as above)
print(word[0:3])  # get the first three char
print(word[:3])  # get the first three char
print(word[-3:])  # get the last three char
print(word[3:])  # get all but the three first char
print(word[:-3])  # get all but the three last character

# Split Strings
word = "Hello World"
print(word.split(' '))  # Split on whitespace

# STARTSWITH/ENDSWITH
word = "hello world"
print(word.startswith("H"))
print(word.endswith("d"))
print(word.endswith("w"))

# REPLACING
word = "Hello World"
print(word.replace("Hello", "Goodbye"))

# CHANGING UPPER AND LOWER CASE STRINGS
string = "Hello World"
print(string.upper())
print(string.lower())
print(string.title())
print(string.capitalize())
print(string.swapcase())

# SERIALIZATION

example_dict = {1: "6", 2: "2", 3: "f"}

pickle_out = open("dict.pickle", "wb")
pc.dump(example_dict, pickle_out)
pickle_out.close()

# pickle_in = open("dict.pickle", "rb")
# example_dict = pc.load(pickle_in)

# print(example_dict)
# print(example_dict[2])

# FILE PATH
# os.path.basename
fldr = os.path.basename(
    "E:\Data_Urang\Mata Kuliah\Semester 3\Pemrograman2\Chapter_9")
print(fldr)
file = os.path.basename(
    "E:\Data_Urang\Mata Kuliah\Semester 3\Pemrograman2\Chapter_9\STRINGS.py")
print(file)

# os.path.dirname
DIR = os.path.dirname(
    "E:\Data_Urang\Mata Kuliah\Semester 3\Pemrograman2\Chapter_9")
print(DIR)
