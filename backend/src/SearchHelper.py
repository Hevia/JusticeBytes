from pybloom import BloomFilter
import re
# from nltk.corpus import wordnet
from typing import List

class SearchHelper:
    def __init__(self, stop_words=[], error_rate=0.1, buffer=100):
        self._filters = {}
        self._error_rate = error_rate
        self._stop_words = stop_words,
        self._buffer = buffer

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
    # Assumes a dictionary of keyword-frequency dictionaries is passed in to work with
    def alt_search(self, search_data_cleaned  : dict, search_string: str) -> str:
        ranked: dict = {}
        # TODO: sanitizing query would improve runtime, but we won't get false negatives.
        search_terms = re.split("\W+", search_string)

        # Adds frequency of the keywords contained both in the url and the search string. 
        for title, words in search_data_cleaned.items():
            rank = 0
            for word in words:
                if word in search_terms:
                    rank += words[word]
            ranked[title] = rank

        # Looks through ranking just made and returns URL w/ highest rank.
        maxVal = 0
        bestURL : str = ""
        for title, ranking in ranked.items():
            if ranking > maxVal:
                maxVal = ranking
                bestURL = title

        return bestURL

    def search(self, search_string: str) -> List[str]:
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
