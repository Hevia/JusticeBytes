# Adam Fernandes
# ShellHacks 2020

# URL bases which will be the beginning of all URLS
WIKI_URL_BASE: str = "https://en.wikipedia.org/wiki/"

# Opens up the political keywords corpus
fileObject = open("keywords.txt", "r")

def scrapeWikipedia():
   for line in fileObject:
      if line == "\n":
         continue
      
      keyword: str = line.strip("\n")
      newUrl: str = WIKI_URL_BASE + keyword

      print(newUrl)

scrapeWikipedia()

# Closes the file before terminating
fileObject.close()