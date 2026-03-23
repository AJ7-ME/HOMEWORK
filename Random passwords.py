import random

#length
length = int(input("Enter password length: "))
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# 
password = ""
for i in range(length):
    password += random.choice(characters)

# Final choice/password/Output
print("Your random password is:", password)