from azure.cognitiveservices.language.luis.authoring import LUISAuthoringClient
from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from msrest.authentication import CognitiveServicesCredentials
from functools import reduce
from typing import List
from etc.FileHelpers import *


class AzureLUISHelper:
    def __init__(self):
        self.credential_dict = loadJSON("./credentials/azure-keys.json")
        self.client = LUISRuntimeClient(
            endpoint=f'https://{self.credential_dict["predictionResourceName"]}.cognitiveservices.azure.com/',
            credentials=CognitiveServicesCredentials(self.credential_dict["predictionKey"])
        )
    
    # TODO: Not sure how the final method signature will look like but heres a start
    def searchLUIS(self, search_query: str) -> List[str]:
        return []

    def makePrediction(self, pred_query: str):
        predictionRequest = {"query": pred_query}
        predictionResponse = self.client.prediction.get_slot_prediction(
            self.credential_dict["appId"], 
            "Development", 
            predictionRequest)
        return predictionResponse.prediction.top_intent
