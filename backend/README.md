# JusticeBytes Backend

## Instructions
* Clone the repo
* Navigate to the backend directory
* We reccommended you create a virtual environment. We use [pipenv](https://pypi.org/project/pipenv/)

Enter this in your command line:
```
pip install pipenv
pipenv shell
pip install -r requirements.txt
```
You can now run the project!. To run the API enter from the backend/ folder enter:
```
cd src/
uvicorn main:app --reload
```
If you run into any errors, make sure you are inside of the src/ directory

You can test the API by hitting out testJSON endpoint. Here is some example dummy data:
```
{
    "search_query":"hello"
}
```
It should echo the data back to you


