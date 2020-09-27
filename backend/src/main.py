from typing import Optional
from fastapi import Body, Request, FastAPI
from pydantic import BaseModel
from SearchHelper import SearchHelper
from AzureLUISHelper import AzureLUISHelper
from BingHelper import BingHelper
from fastapi.middleware.cors import CORSMiddleware


# init our API
app = FastAPI()

# add our app middleware
origins = [
    "http://localhost:3000",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# init our helpers and data sources
searchHelper = SearchHelper()
azureHelper = AzureLUISHelper()
bingHelper = BingHelper()

# init our data models
class SearchData(BaseModel):
    search_query: str

# You can use this to test if the server is alive
@app.get("/")
def ping():
    return {"Hello": "World"}

@app.post("/request")
async def testRequest(req: Request):
    print(await req.body())
    return {"Hello": "World"}

# Use this method to debug if the server is accepting JSON
@app.post("/testJSON")
def testJSON(searchData: SearchData):
    print(searchData)
    return searchData

@app.post("/search")
def search(searchData: SearchData):
    search_query = searchData.search_query
    search_results = []

    # Using our handwritten search algorithim, well see if we can return any documents
    try:
        custom_search = searchHelper.search(search_query)
        search_results = search_results + custom_search
    except Exception:
        print(f"Error on vanilla search with query: {search_query} ")

    print(f"Here is what the search results look like: {search_results}")

    return {"search_results": search_results}
    