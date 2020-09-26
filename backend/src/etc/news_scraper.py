# Adam Fernandes
# ShellHacks 2020
#
# Scrapes news websites based on a list of keywords; Outputs a dict with key
# being keyword and value being a double array consisting of URL, article title

from newsapi import NewsApiClient
from FileHelpers import load_file_as_list, pickleObject

# Adam's alternate email API Key
API_KEY: str = "37eee34b3156415680064022caa7c23b"
# File holding keywords
KEYWORDS_FILENAME: str = "keywords.txt"
# Output file
PICKLE_FILENAME: str = "scraped-news.pickle"

def scrapeNews(filename: str) -> dict:
   """
   Utilizes NewsApiClient to return a dict containing keywords as key
   and a double array with URL, article title as value
   """

   newsapi: NewsApiClient = NewsApiClient(API_KEY)
   inputLines: list = load_file_as_list(filename)
   
   output: dict = {}

   for line in inputLines:      
      line = line.strip("\n")
      print(line)

      newsResults: dict = newsapi.get_everything(q=line, qintitle=None, sources="cnn, abc-news, google-news-au, politico, new-york-times, bbc-news", language="en")
      
      if (newsResults["totalResults"] > 1):
         output[line] = []
         
         for article in newsResults["articles"]:  
            tempData: list = [article["url"], article["title"]]
            output[line].append(tempData)
   
   return output

output: dict = scrapeNews(KEYWORDS_FILENAME)
pickleObject(PICKLE_FILENAME, output)