# JusticeBytes Backend

## Local Instructions
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
It should echo the data back to you, if it does. Congrats! You are now ready for local development


## Docker Instructions
* Install Docker to your machine
* Clone the repo
* Navigate to the backend/ directory

Build the docker image
```
docker build -t justicebytes-backend .
```

Run the image
```
docker run -p 8000:8000 justicebytes-backend
```