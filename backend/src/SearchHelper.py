from pybloom import BloomFilter
import pickle
import re
import requests
from etc.FileHelpers import *
import json
from BingHelper import BingHelper
# from nltk.corpus import wordnet
from typing import List

class SearchHelper:
    def __init__(self, stop_words=[], error_rate=0.1, buffer=100):
        self._filters = {}
        self._error_rate = error_rate
        self._stop_words = stop_words,
        self._buffer = buffer
        self.bingHelper = BingHelper()

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

        if (len(response["flaggedTokens"]) == 0):
            return search_terms
        
        #print(response)
        
        
        for x in range(len(search_terms)):
            if (search_terms[x] == response["flaggedTokens"][i]["token"]):
                search_terms[x] = response["flaggedTokens"][i]["suggestions"][0]["suggestion"]
                i += 1

        #print(search_terms)
        
        return search_terms

    # Assumes a dictionary of keyword-frequency dictionaries is passed in to work with
    def search(self, search_string: str) -> str:
        
        
        # TODO: sanitizing query would improve runtime, but we don't get false negatives right now.
        search_terms = self.spellCheck(search_string)
        ranked: dict = {}
        
        pickle_in = open("./etc/scraped-wikipedia-output.pickle", "rb")
        search_data_cleaned = pickle.load(pickle_in)
        
        
        # Adds frequency of the keywords contained both in the article and the search string. 
        for title, words in search_data_cleaned.items():
            rank = 0
            for word, freq in words.items():
                if word in search_terms:
                    rank += freq
            if (rank > 0):
                ranked[title] = rank
        print(ranked)
        
        # Looks through ranking just made and returns URL w/ highest rank.
        maxVal = 0
        bestURL: str = ""
        for title, ranking in ranked.items():
            if ranking > maxVal:
                maxVal = ranking
                bestURL = title

        print(bestURL)
        pickle_in.close()

        return bestURL

    

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
