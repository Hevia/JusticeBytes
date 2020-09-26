# Adam Fernandes
# ShellHacks 2020
# Opens up a pickle file

import pickle

PICKLE_FILENAME: str = "scraped-wikipedia-output.pickle"

# Unpickles a file and returns the object
def unpickle(filename: str) -> object:
   pickleIn = open(filename, "rb")
   pickledObject = pickle.load(pickleIn)
   pickleIn.close()
   return pickledObject

obj: object = unpickle(PICKLE_FILENAME)