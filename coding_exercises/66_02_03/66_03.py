# Write a program that reads the essay.txt file and returns the number of characters contained in the file.

file = open("essay.txt", 'r')
essay_text = file.read()
file.close()

print(len(essay_text))
