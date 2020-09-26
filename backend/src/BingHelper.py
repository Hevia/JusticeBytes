from azure.cognitiveservices.search.newssearch import NewsSearchClient
from msrest.authentication import CognitiveServicesCredentials
from etc.FileHelpers import *

class BingHelper:
    def __init__(self):
        self.credential_dict = loadJSON("./credentials/azure-keys.json")