# Adam Fernandes
# ShellHacks 2020
# Quick and dirty script for cleaning previous data

from FileHelpers import load_file_as_list

TARGET_FILE: str = "keywords.txt"

# Read file
rawInput = load_file_as_list(TARGET_FILE)
noiceInput = []

for item in rawInput:
   s = item
   newS = item.split(", ")
   noiceInput.append(newS)

# Writing back into file
try:
   with open(TARGET_FILE, "w") as fileObject:
      for item in noiceInput:
         for string in item:
            fileObject.write(string + "\n")
except Exception:
   raise Exception(f"Error writing to file at: {TARGET_FILE}")