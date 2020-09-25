from pybloom import BloomFilter
import re
from nltk.corpus import wordnet
from typing import List

class SearchHelper:
    def __init__(self, stop_words=[], error_rate=0.1, buffer=100):
        self._filters = {}
        self._error_rate = error_rate
        self._stop_words = stop_words,
        self._buffer = buffer

    def add_search_data(self, search_data_cleaned: dict) -> None:
        for title, words in search_data_cleaned.items():
            self._filters[title] = BloomFilter(capacity=len(words)+self._buffer, error_rate=self._error_rate)
            for word in words:
                if word in self._stop_words:
                    pass
                else:
                    self._filters[title].add(word)

    def search(self, search_string: str) -> List[str]:
        search_terms = re.split("\W+", search_string)
        return [name for name, _filter in self._filters.items() if all(term in _filter for term in search_terms)]

    def semantic_search(self) -> List[str]:
        pass

    def _find_synonyms(self, words: List[str]) -> List[str]:
        synonyms = []
        for word in words:
            try:
                synonyms.append(wordnet.synsets(word))
            except Exception:
                print(f"Error finding synonyms on word: {word}")
        
        return synonyms

    def _preprocess_search_query(self):
        pass