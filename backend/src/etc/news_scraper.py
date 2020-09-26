# Adam Fernandes
# ShellHacks 2020
# Scrapes news websites based on a list of keywords and outputs URLs of articles and short blurbs

from bs4 import BeautifulSoup
import requests
from FileHelpers import load_file_as_list

KEYWORDS_FILENAME: str = "keywords.txt"

class NewsScraper():
   # Constructor takes in an input file for keyword searches
   def __init__(self, filename: str):
      self.inputLines: list = load_file_as_list(filename)
      self.soup: BeautifulSoup
      for line in self.inputLines:
         line = line.strip("\n")

   # Returns true if a link is valid, false otherwise
   def isValidLink(self, link: requests.models.Response) -> bool:
      try:
         link.raise_for_status()
      except:
         return False
      return True
   
   # Constructs a link to an NPR search based on the string argument
   def constructNPRLink(self, input: str) -> str:
      strList: list = input.split()
      if len(strList) <= 0 or strList[0] == "\n":
         return ""
      linkArgument: str = strList[0]

      for i in range(1, len(strList)):
         linkArgument += "%20" + strList[i]

      nprBaseLink: str = "https://www.npr.org/search?query=%s&page=1" % (linkArgument)
      return nprBaseLink

   # Scrapes NPR for information based on keywords and returns dictionary
   # Key: Keyword: str, Value: (Article Title, URL): tuple
   def scrapeNPR(self):
      testing: int = 0


      for line in self.inputLines:
         testing += 1
         
         line = line.strip("\n")
         nprLink = self.constructNPRLink(line)
         if nprLink == "":
            continue
         
         link: requests.models.Response = requests.get(self.constructNPRLink(line))
         if self.isValidLink(link):
            print(nprLink)
         else:
            continue
         
         self.soup = BeautifulSoup(link.text, "html.parser")
         print(self.soup.prettify())
         info = self.soup.find_all(attrs={'class': 'ais-InfiniteHits-item'})
         try:
            print(info.get_text())
         except:
            print("oof")

         if testing == 2:
            break         

scraper = NewsScraper(KEYWORDS_FILENAME)
scraper.scrapeNPR()