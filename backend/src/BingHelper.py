from azure.cognitiveservices.search.newssearch import NewsSearchClient
from msrest.authentication import CognitiveServicesCredentials
from etc.FileHelpers import *
import requests

class BingHelper:
    def __init__(self):
        self.credential_dict = loadJSON("./credentials/azure-keys.json")

    def spellCheckerRequest(self, search_string : str) -> requests.models.Response:
        api_key = "1dda35b6c6f844eba04f46df2bdb1da6"
        example_text = "Hollo, wrld" # the text to be spell-checked
        endpoint = "https://api.cognitive.microsoft.com/bing/v7.0/SpellCheck"
        data = {"text" : search_string}
        params = {
        'mkt':'en-us',
        'mode':'proof'
        }
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Ocp-Apim-Subscription-Key': api_key,
        }

        return requests.post(endpoint, headers=headers, params=params, data=data)

