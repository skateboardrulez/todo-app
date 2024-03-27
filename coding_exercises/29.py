# Write a program that:
# 1. asks users to enter a password.
# 2. returns "Great password there!" if the password has more than 7 characters. For example:
# 3. returns "Your password is weak." if the password has 7 or fewer characters. For example:

password = input("Enter a new password: ")

if len(password) <= 7:
    print("Your password is weak.")
else:
    print("Great password there!")
