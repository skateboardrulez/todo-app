# On the side panel there's a bear.txt file. The existing code opens that file in read mode.
#
# Below that code, please read the file content and print out the content.


file = open("bear.txt", 'r')
bear_text = file.read()
file.close()
print(f"{bear_text}")
