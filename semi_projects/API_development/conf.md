Tools

1. FastAPI
2. Postman(testing tool)
3. SQL

# Virtual Environment Setting

* Create venv

```
py -3 -m venv [venv name]
```

* Select path to the interpreter

  -view -> command pallet-> python select interpreter, then type .\venv\Scripts\python.exe to activate the venv's interpreter

* activate the venv

```
.\venv\Scripts\activate.bat
```

# Fast API Installation

```
pip install fastapi[all]
```

* Add the fastapi code in main.py

```python
from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

* run the server

```
uvicorn main:app
# main is the script file and app is the object 

# or we coud use reload option so it will refresh the codes and apply it to the page
uvicorn main:app --reload
```

# Requests

* get reqeust: to retrieve the data from the API server.
* post request: posting a data in the API server
* To see post request, type the code below and post request to http://127.0.0.1:8000/createposts

```python
# catch the post data and print it out
@app.post("/createposts")
# body data will be converted into dict form of payload variable
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"message": "successfully created posts"}

# or

@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title: {payload['title']} content: {payload['content']}"}
```

# Schema

We will use a library called pydantic to restrict the type of data to be received.

```python
from typing import Optional
from pydantic import BaseModel

# this Post 
class Post(BaseModel):
    title: str
    content: str
    published: bool = True  # This is an optional data, when we set default as True
	rating: Optional[int] = None  # takes int and returns None when no data received
        
@app.post("/createposts")
def create_posts(post: Post):
    # new_post is the parameter and Post is the class to determine parameter's type.
    print(post)
    print(post.dict()) # to save post data into dict type
    # or print(new_post.title) to extract title data
    return {"data": "post"}

```

