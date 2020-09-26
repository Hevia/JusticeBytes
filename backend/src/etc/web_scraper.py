# Adam Fernandes
# ShellHacks 2020

from bs4 import BeautifulSoup
import requests

TEST = True

# URL bases which will be the beginning of all URLS
WIKI_URL_BASE: str = "https://en.wikipedia.org/wiki/"
# Filename holding political keywords from https://myvocabulary.com/word-list/politicsvocabulary/
KEYWORDS_FILENAME: str = "keywords.txt"
# Read from the keywords file
fileObject = open(KEYWORDS_FILENAME, "r")

# Returns a dictionary where keys are keywords and values are frequencies (initialized to 0)
def createFrequencyKeywordsDict() -> dict:   
   freqDict: dict = {}
   
   for line in fileObject:
      if line == "\n":
         continue
      line = line.strip("\n").lower()
      freqDict.setdefault(line, 0)
   
   fileObject.seek(0)
   return freqDict

# Returns true if a link is a valid webpage, false otherwise
def isValidLink(link: requests.models.Response) -> bool:
   try:
      link.raise_for_status()
   except:
      print("Error in %s." % (link))
      return False
   return True

# Goes ahead and increments values inside the heatmap
def incrementFrequencies(info, heatmap: dict):
   for word in info.get_text().split(" "):
      word = word.rstrip(",").rstrip(".").strip("\"").lower()
      if word in heatmap:
         heatmap[word] += 1

# Edits heatmap based on the tag element's contents
# In other words, increments values in heatmap if a word is found within tag element or its siblings
def editHeatmap(info, heatmap: dict) -> dict:
   # Once for Tag object itself
   incrementFrequencies(info, heatmap)
   
   # Now for all the siblings
   for sibling in info.next_siblings:
      try:
         incrementFrequencies(sibling, heatmap)
      except:
         break
   
   return heatmap

# Uses the keywords from the corpus to scrape Wikipedia
# Returns a dictionary where key is URL and value is a heat map of other words in the dictionary
def scrapeWikipedia() -> dict:
   # TESTING
   test: int = 0

   scrapedInfo: dict = {}
   freqDict: dict = createFrequencyKeywordsDict()

   for line in fileObject:
      if line == "\n":
         continue
      
      keyword: str = line.strip("\n")
      newUrl: str = WIKI_URL_BASE + keyword
      link: requests.models.Response = requests.get(newUrl)

      if not isValidLink(link):
         continue
      
      soup: BeautifulSoup = BeautifulSoup(link.content, "html.parser")
      
      info = soup.select_one("div div p")
      heatmap: dict = editHeatmap(info, freqDict.copy())

      print(heatmap)
      
      print("********************************************************************************")
      
      # TESTING
      if TEST:
         test += 1
         if (test > 2):
            break

# Method Calls
scrapeWikipedia()

# Closes file before ending program
fileObject.close()