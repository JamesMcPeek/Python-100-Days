import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print ("Welcome to the PyPassword Generator!")

userLetters = int(input("How many letters would you like in your password?\n"))
userSymbols = int(input("How many symbols would you like in your password?\n"))
userNumbers = int(input("How many numbers would you like in your password?\n"))

passwordList = []

for char in range(1, userLetters + 1):
    passwordList.append(random.choice(letters))

for char in range(1, userSymbols + 1):
    passwordList.append(random.choice(symbols))

for char in range(1, userNumbers + 1):
    passwordList.append(random.choice(numbers))

random.shuffle(passwordList)

password = ""
for char in passwordList:
    password += char

print(f"Your password is: {password}")
