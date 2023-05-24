# Password Generator Project

import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

sequence = []

for letterIndex in range(1, nr_letters + 1):
    i = random.randint(0, len(letters) - 1)
    letter = letters[i]
    sequence.append(letter)

for symbolIndex in range(1, nr_symbols + 1):
    i = random.randint(0, len(symbols) - 1)
    symbol = symbols[i]
    sequence.append(symbol)

for numberIndex in range(1, nr_numbers + 1):
    i = random.randint(0, len(numbers) - 1)
    number = numbers[i]
    sequence.append(number)

random.shuffle(sequence)
random_str = ""
random_pw = random_str.join(sequence)

print(f"Your password is: {random_pw}")

