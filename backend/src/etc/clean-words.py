# Adam Fernandes
# ShellHacks 2020
# Quick and dirty script for cleaning previous data

# Read file
fileObject = open("keywords.txt", "r")

rawInput = fileObject.readlines()
noiceInput = []

for item in rawInput:
   s = item
   newS = item.split(", ")
   noiceInput.append(newS)

fileObject.close()

# Writing back into file
fileObject = open("keywords.txt", "w")

for item in noiceInput:
   for string in item:
      fileObject.write(string + "\n")

fileObject.close()