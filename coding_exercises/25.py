# Extend the given code (in the exercise area) so the code capitalizes all the names and surnames of the list and
# then prints the new list. The output of your code should be as below:
#
# ['John Smith', 'Jay Santi', 'Eva Kuki']

names = ["john smith", "jay santi", "eva kuki"]

cap_names = [item.title() for item in names]
print(cap_names)
