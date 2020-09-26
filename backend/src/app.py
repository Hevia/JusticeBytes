from typing import Optional
from fastapi import FastAPI
from SearchHelper import SearchHelper
from AzureHelper import AzureHelper

# init our API
app = FastAPI()

# init our helpers
searchHelper = SearchHelper()
azureHelper = AzureHelper()

# You can use this to test if the server is alive
@app.get("/")
def ping():
    return {"Hello": "World"}


@app.get("/search")
def search():
    search_query = "" #TODO: Get this from the JSON body, this is place holder
    search_results = []

    # Using our handwritten search algorithim, well see if we can return any documents
    try:
        vanilla_search = searchHelper.search(search_query)
        search_results = search_results + vanilla_search
    except Exception:
        print(f"Error on vanilla search with query: {search_query} ")

    try:
        # TODO: Actually implement LUIS functionality
        luis_search = azureHelper.searchLUIS(search_query)
        search_results = search_results + luis_search
    except Exception:
        print(f"Error on LUIS search with query: {search_query} ")

    print(f"Here is what the search results look like: {search_results}")

    return {"search_results": search_results}
    