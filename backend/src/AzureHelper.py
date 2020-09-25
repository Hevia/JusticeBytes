from azure.cognitiveservices.language.luis.authoring import LUISAuthoringClient
from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from msrest.authentication import CognitiveServicesCredentials
from functools import reduce
from typing import List
import json, time


class AzureHelper:
    def __init__(self):
        # TODO: Authenticate with Azure LUIS here
        pass
    
    # TODO: Not sure how the final method signature will look like but heres a start
    def searchLUIS(self, search_query: str) -> List[str]:
        pass