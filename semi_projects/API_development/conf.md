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

# CRUD application

Create, Read, Update, Delete acronym

* Create -> POST -> /posts -> @app.post('/posts')
* Read -> GET /posts/:id -> @app.get("/posts/{id}")
* Read -> GET /posts -> @app.get("/posts")
* Update -> PUT/PATCH -> /posts/:id -> @app.put("/posts/{id}") # PUT needs all other data whereas PATCH only needs only the data for the specific field.(e.g. when updating title, PUT needs title and body all. PATCH only needs title)
* Delete -> DELETE -> /posts//:id -> @app.delete("/posts/{id}")



Make an hard-coded data in my_posts variable and return this data. If I try GET http://127.0.0.1:8000/posts, my_posts will appear.

```python
my_posts = [{"title": "title of post 1", "content": "content 1", "id": 1},
            {"title": "facorite foods", "content": "i like pizza", "id": 2}]

@app.get("/posts")
def get_posts():
    return {"data": my_posts}
```

# Giving ID to the post

To give ID a random number, random lib is called for practice purpose.

```python
from random import randrange

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}
```

