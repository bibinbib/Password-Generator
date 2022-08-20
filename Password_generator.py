#Password Generator Project
# importing the random module
import random

# Uppercase and Lower case Alphabets
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# The numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# The Special character symbols
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Generating the message to the user and getting inputs from the user
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pass_list=[]

for char in range(1, nr_letters+1):
  pass_list += random.choice(letters)
for char in range(1,nr_symbols+1):
  pass_list += random.choice(symbols)
for char in range(1,nr_numbers+1):
  pass_list += random.choice(numbers)

# printing the password list as enterd form by the user
print(pass_list)
# using the shuffle fuction to randomize the characters inside the pass_list
random.shuffle(pass_list)
# displaying the shuffled pass_list 
print(pass_list)
password=""
# convering the pass_list list into Strings
for characters in pass_list:
  password+=characters
# displaying the password as string
print(f"\n Your password is : {password}")