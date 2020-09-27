from BingHelper import BingHelper
import pickle
from pybloom import BloomFilter
import re
import requests
from typing import List

class SearchHelper:
    def __init__(self, stop_words=[], error_rate=0.1, buffer=100):
        self._filters = {}
        self._error_rate = error_rate
        self._stop_words = stop_words,
        self._buffer = buffer
        self.bingHelper = BingHelper()
        self.bingNewsResultsNumber = 10

    def add_search_data(self, search_data_cleaned: dict) -> None:
        # Takes the title and list of words from the map.
        for title, words in search_data_cleaned.items():
            # Creates a bloom filter @ filters[title] where capacity is length of words and the given error rate.
            self._filters[title] = BloomFilter(capacity=len(words)+self._buffer, error_rate=self._error_rate)
            for word in words:
                # If a word isn't in stopWords array, add it to the bloom filter.
                if word in self._stop_words:
                    pass
                else:
                    self._filters[title].add(word)
                 
    def spellCheck(self, search_string: str) -> []:
        response = (self.bingHelper.spellCheckerRequest(search_string)).json()
        search_terms = re.split("\W+", search_string)
        i = 0
        
        # If all the words are spelled correctly in the query, just return the terms split on whitespace.
        if (len(response["flaggedTokens"]) == 0):
            return search_terms
        
        # Goes through and replaces misspelled words with their corrected spelling.
        for x in range(len(search_terms)):
            if (search_terms[x] == response["flaggedTokens"][i]["token"]):
                search_terms[x] = response["flaggedTokens"][i]["suggestions"][0]["suggestion"]
                i += 1
        
        return search_terms

    # Creates an array of dicts from a list of tuples
    def Convert(self, tup, di) -> dict:
        array = [] 
        for a, b in tup:
            di = {}
            di["url"] = a
            di["title"] = b 
            array.append(di) 
        return array

    # Assumes a dictionary of keyword-frequency dictionaries is passed in to work with
    def search(self, search_string: str) -> dict:
        # TODO: sanitizing query would improve runtime, but we don't get false negatives right now.
        search_terms = self.spellCheck(search_string)
        result = []
        dictionary = {}

        pickle_in = open("./etc/scraped-news.pickle", "rb")
        search_data_cleaned = pickle.load(pickle_in)

        # Adds the url and title as a single element, we return the collection of them as an n x 2 array.
        for keyword, value in search_data_cleaned.items():
                if (keyword in search_terms):
                    for x in range(len(value)):
                        result.append(value[x])

        response = self.bingHelper.newsRequest(search_string, self.bingNewsResultsNumber)
        
        # Appends the name and URL from the Bing news articles to the results.
        for x in response.value:
            result.append([x.url, x.name])
        
        pickle_in.close()

        return self.Convert(list(set(map(tuple, result))), dictionary)

    def alt_search(self, search_string: str) -> List[str]:
        search_terms = re.split("\W+", search_string)
        
        # Returns the name if all terms in the filter are also contained in the search terms.
        return [name for name, _filter in self._filters.items() if all(term in _filter for term in search_terms)]

    def semantic_search(self) -> List[str]:
        pass

    # TODO: Decide if were doing this or not
    def _find_synonyms(self, words: List[str]) -> List[str]:
        synonyms = []
        # for word in words:
        #     try:
        #         synonyms.append(wordnet.synsets(word))
        #     except Exception:
        #         print(f"Error finding synonyms on word: {word}")
        
        return synonyms

    def _preprocess_search_query(self):
        pass