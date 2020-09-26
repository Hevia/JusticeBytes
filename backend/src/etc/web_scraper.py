# Adam Fernandes
# ShellHacks 2020

from bs4 import BeautifulSoup
import requests

TEST = False

# URL bases which will be the beginning of all URLS
WIKI_URL_BASE: str = "https://en.wikipedia.org/wiki/"
# Filename holding political keywords from https://myvocabulary.com/word-list/politicsvocabulary/
KEYWORDS_FILENAME: str = "keywords.txt"

# Opens up the political keywords corpus
fileObject = open(KEYWORDS_FILENAME, "r")

# Returns true if a link is a valid webpage, false otherwise
def isValidLink(link: requests.models.Response):
   try:
      link.raise_for_status()
   except:
      print("Error in %s." % (link))
      return False
   return True

# Uses the keywords from the corpus to scrape Wikipedia
# Returns a dictionary where key is URL and value is a heat map of other words in the dictionary
def scrapeWikipedia():
   # TESTING
   test: int = 0
   
   scrapedInfo: dict = {}

   for line in fileObject:
      if line == "\n":
         continue
      
      keyword: str = line.strip("\n")
      newUrl: str = WIKI_URL_BASE + keyword
      link: requests.models.Response = requests.get(newUrl)

      if not isValidLink(link):
         continue
      
      soup = BeautifulSoup(link.content, "html.parser")
      info = soup.select_one("div div p")
      print(info.text)
      for sibling in info.next_siblings:
         try:
            print(sibling.get_text())
         except:
            break
      print("********************************************************************************")
      # TESTING
      if TEST:
         test += 1
         if (test > 2):
            break


scrapeWikipedia()

# Closes the file before terminating
fileObject.close()