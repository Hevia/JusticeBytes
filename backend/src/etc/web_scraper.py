# Adam Fernandes
# ShellHacks 2020

import requests

# URL bases which will be the beginning of all URLS
WIKI_URL_BASE: str = "https://en.wikipedia.org/wiki/"
# Filename holding political keywords from https://myvocabulary.com/word-list/politicsvocabulary/
KEYWORDS_FILENAME: str = "keywords.txt"

# Opens up the political keywords corpus
fileObject = open(KEYWORDS_FILENAME, "r")

# Returns true if a link is a valid webpage, false otherwise
def isValidLink(link: str):
   website = requests.get(link)

   try:
      website.raise_for_status()
   except:
      print("Error in %s." % (link))
      return False
   
   return True

# Uses the keywords from the corpus to scrape Wikipedia
def scrapeWikipedia():
   for line in fileObject:
      if line == "\n":
         continue
      
      keyword: str = line.strip("\n")
      newUrl: str = WIKI_URL_BASE + keyword

      isValidLink(newUrl)

scrapeWikipedia()

# Closes the file before terminating
fileObject.close()