# Adam Fernandes
# ShellHacks 2020
# Scrapes Wikipedia based on a list of keywords and outputs a heatmap of frequencies to a pickle file

from bs4 import BeautifulSoup
from FileHelpers import pickleObject
import pickle
import requests

# Toggle t/f for debugging purposes
DEBUGGING = False

# URL bases which will be the beginning of all URLS
WIKI_URL_BASE: str = "https://en.wikipedia.org/wiki/"
# Filename holding political keywords from https://myvocabulary.com/word-list/politicsvocabulary/
KEYWORDS_FILENAME: str = "keywords.txt"
# Filename of output pickle file
PICKLE_FILENAME: str = "scraped-wikipedia-output.pickle"
# Read from the keywords file
fileObject = open(KEYWORDS_FILENAME, "r")

def createFrequencyKeywordsDict() -> dict:   
   """
   Returns a dictionary where keys are keywords and values are frequencies (initialized to 0)
   """
   
   freqDict: dict = {}
   
   for line in fileObject:
      if line == "\n":
         continue
      line = line.strip("\n").lower()
      freqDict.setdefault(line, 0)
   
   fileObject.seek(0)
   return freqDict

def isValidLink(link: requests.models.Response) -> bool:
   """
   Returns true if a link is a valid webpage, false otherwise
   """

   try:
      link.raise_for_status()
   except:
      if DEBUGGING:
         print("Error in %s." % (link))
      return False
   return True

def incrementFrequencies(info, heatmap: dict) -> None:
   """
   Goes ahead and increments values inside the heatmap
   """

   for word in info.get_text().split(" "):
      word = word.rstrip(",").rstrip(".").strip("\"").lower()
      if word in heatmap:
         heatmap[word] += 1

def editHeatmap(info, heatmap: dict) -> dict:
   """
   Edits heatmap based on the tag element's contents
   In other words, increments values in heatmap if a word is found within tag element or its siblings
   """
   
   # Once for Tag object itself
   incrementFrequencies(info, heatmap)
   
   # Now for all the siblings
   for sibling in info.next_siblings:
      try:
         incrementFrequencies(sibling, heatmap)
      except:
         break
   
   return heatmap

def scrapeWikipedia() -> dict:
   """
   Uses the keywords from the corpus to scrape Wikipedia.
   Returns a dictionary where key is URL and value is a heat map of other words in the dictionary
   """
   
   # DEBUGGING
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

      scrapedInfo[newUrl] = heatmap
            
      if DEBUGGING:
         test += 1
         if (test > 2):
            return scrapedInfo
   
   return scrapedInfo

# Method Calls
output = scrapeWikipedia()
pickleObject(PICKLE_FILENAME, output)

# Closes file before ending program
fileObject.close()