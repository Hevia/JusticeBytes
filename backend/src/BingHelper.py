from azure.cognitiveservices.search.newssearch import NewsSearchClient
from msrest.authentication import CognitiveServicesCredentials
from etc.FileHelpers import *
import requests

class BingHelper:
    def __init__(self):
        self.credential_dict = loadJSON("./credentials/azure-keys.json")
        self.client = NewsSearchClient(
            endpoint=f'https://{self.credential_dict["bingSearchName"]}.cognitiveservices.azure.com/',
            credentials=CognitiveServicesCredentials(self.credential_dict["bingSearchAPIKey"]))

    def spellCheckerRequest(self, search_string : str) -> requests.models.Response:
        api_key = self.credential_dict["spellCheckAPIKey"]
        endpoint = "https://api.cognitive.microsoft.com/bing/v7.0/SpellCheck"
        data = {"text" : search_string} # the text to be spell-checked
        params = {
        'mkt':'en-us',
        'mode':'proof'
        }
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Ocp-Apim-Subscription-Key': api_key,
        }

        return requests.post(endpoint, headers=headers, params=params, data=data)

    def newsRequest(self, search_string: str, count: int) -> requests.models.Response:
        return self.client.news.search(query = search_string, market = "en-us", count = count)

