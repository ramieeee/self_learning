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

# POST

## Giving ID to the post

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

# GET

To get the specific post using id, we could use the path as `/posts/{id}`, and set the parameter as `id: int` so it will automatically convert the parameter into integer.

```python
def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

# path parameter
@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    return {"post_detail": post}
```

# Error exceptions

Raise an 404 error when post not found.

```python
from fastapi import FastAPI, Response, status, HTTPException

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return {"post_detail": post}
```

Also send 201 status when post is created.

```python
@app.post("/posts", status_code=status.HTTP_201_CREATED)
```

# DELETE

Deleting sends 204 status. 

```python
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
```

# UPDATE

The flow of update is as below.

1. look for index. if not index, raise an error
2. convert post in JSON type into regular python dict type
3. change the original post into the new post `my_posts[index] = post_dict`

```python
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)
        
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"data": post_dict}
```

# Built-in documentation

FastAPI automatically update documentation.

`http://127.0.0.1:8000/docs` shows the SwaggerUI

`http://127.0.0.1:8000/redoc` also is a different type of documentation

# Packaging

* Create a folder that reads `app`
* move `main.py` into `app` folder
* create `__init__.py` file in `app` folder
* `uvicorn app.main:app --reload` command will search the path ./app/main.py

# Database

* We don't work or interact with db directly.
* SQL will be used to communicate with DBMS

# Postgres

It can create multiple separate databases

* Install PostgreSQL Server, gpAdmin 4
* default port is 5432
* When creating a server, super user is postgres
* tables at pgAdmin 4: database -> schemas -> public -> table
* data type `serial`: it is a randomely created number to act as id

When using Postgres with Python, it needs a driver.

# Database

* A table represents a subject or event in an application
* All data tables are related to one another
* Each Column represents a different attribute
* Each row represents a different entry in the table
* Databases have datatypes like any other programming languages

| Data Type | Postgres                | Python     |
| --------- | ----------------------- | ---------- |
| Numeric   | int, decimal, precision | int, float |
| Text      | Varchar, text           | string     |
| bool      | boolean                 | boolean    |
| sequence  | array                   | list       |

# Primary key

* a column or a group of columns that uniquely identifies each row in a table
* Table can have one and only one primary key
* The primary key does not have to be the ID column. A table may not contain the primary key column
* email column could be the primary key column

# Unique Constraints

* Unique constraint can be applied to any column to make sure every record has a unique value for that column(e.g. I could make a blizzard ID but a game character name cannot be duplicate)

# Null Constraints

* by default, postgres allows a black data
* a NOT NULL constraint can be added to the column to ensure that the column is not left blank

# Query

* selecting data from a table

```sql
# all
SELECT * FROM products;

# few columns
SELECT name, id, price FROM products;

# rename column
SELECT it AS products_id FROM products;

# select according to conditions
SELECT * FROM products WHERE id = 10;
SELECT * FROM products WHERE name = 'TV';
SELECT * FROM products WHERE price < 80;
SELECT * FROM products WHERE inventory > 0 AND price > 20;
SELECT * FROM products WHERE price > 100 OR price < 20;

# multiple selection
SELECT * FROM products WHERE id IN (1,2,3);

# LIKE
SELECT * FROM products WHERE name LIKE 'TV%'; # where name starts with 'TV'
SELECT * FROM products WHERE name NOT LIKE '%en%'; # all that does not include 'en'
```

* `not` query

```sql
SELECT * FROM products WHERE inventory <> 0;
# or
SELECT * FROM products WHERE inventory != 0;
```

* ORDER(sorting)

```sql
SELECT * FROM products ORDER BY price ASC;
SELECT * FROM products ORDER BY price DESC;

# first sort inventry, and when inventory is in a tie, then ORDER BY price ASC
SELECT * FROM products ORDER BY inventory DESC, price;

SELECT * FROM products WHERE price > 20 ORDER BY created_at DESC;
```

* LIMIT, OFFSET

```sql
# data retrieving limitation
SELECT * FROM products WHERE price > 10 LIMIT 2;

# OFFSET
SELECT * FROM products ORDER BY id LIMIT 5 OFFSET 3; #skip first 3 rows and limit 5
```

# INSERT data

```sql
# in products table, name/price/inventory columns, the value would be tortilla, 4, 1000
INSERT INTO products (name, price, inventory) VALUES ('tortilla', 4, 1000);
```

* INSERT 0 1 means everything is successful.

```sql
# returning shows the inserted data at the same time of its creation
INSERT INTO products (price, name, inventory) VALUES (10000, 'car', 1000) returning *;

# or
INSERT INTO products (price, name, inventory) VALUES (10000, 'car', 1000), (50, 'laptop', 25), (60, 'monitor', 4) returning id, created_at, name;
```

# DELETE data

```sql
# for example
DELETE FROM products WHERE id = 10;
DELETE FROM products WHERE id = 11 RETURNING *;
```

# UPDATE data

```sql
UPDATE products SET name = 'flour tortilla', price = 40 WHERE id = 20;
UPDATE products SET is_sale = true WHERE id = 22 RETURNING *;
```

# Connecting to DB

We need psycopg2 to connect to DB using python.

```
pip install psycopg2
```

Try connection in the while loop until it is successful to connect.

```python
import psycopg2
from psycopg2.extras import RealDictCursor

# the conn code below is a hard coding and we need to fix the environment for that
while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='password', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)
        time.sleep(2)
```

# Retrieving posts from postgres

```python
@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""") # execute SQL query
    posts = cursor.fetchall() # call data from query into posts var
    return {"data": posts}
```

# Created posts using postgres

```python
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    # it could be f string format but vulnerable to SQL injection. This passing value method is safe
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""", (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit() # to actually safe the data into postgres, commit is a must
    return {"data": new_post}
```

# Retrieving a post with an ID from postgres

```python
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id))) # change id to str for datatype issue
    post = cursor.fetchone() # only fetch one specific post, not fetchall()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return {"post_detail": post}
```

# Deleting a post from postgres

```python
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute("""DELETE FROM posts WHERE id = %s returning *""", (str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
```

# ORM(Object Relational Mapper)

* Layer of abstraction that sits between the DB and us
* performs all database operations through traditional python code(No SQL)
* Sqlalchemy is one of the most popular python ORMs

# sqlalchemy

* sqlalchemy needs psycopg to connect to the db

```
# installation
pip install sqlalchemy
touch database.py
```

```python
# write in database.py file

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# dependancy
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-addr/hostname>/<database_name>'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
```

* models in python code will work as tables of SQL

```python
# store models in models.py
# touch models.py

from sqlalchemy import Column, Integer, String
from .database import Base
class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default = True)
```

```python
# in the main.py file

import sqlalchemy.orm import Session
from . import models
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)
        
@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    return {"status": "success"}
```

