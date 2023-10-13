from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

origins = ["http://localhost:3000"]

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

#create api object
app = FastAPI() 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#end point
#URL/URI
#URL/ENDPOINT
'''In the context of web APIs, endpoints are often URLs that define the API's actions 
and provide a structured way to interact with the service
GET       -obtain information
POST      -add new data
PUT       -update data
DELETE    -delete data 
'''

# # http://127.0.0.1:8000/ will return {"Data": "Hello World"}
# @app.get("/")
# def index():
#     return {"Data": "Hello World"} # this will return as JSON at the endpoint

# # http://127.0.0.1:8000/about will return {"Data": "About Page"}
# @app.get("/about")
# def about():
#     return {"Data": "About Page"}

# create a JSON of inventory
inventory = {
    1:{
        "name": "Mac",
        "price": 1000,
        "brand": "Apple"
    }
}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="The ID of the item you would like to use")): # define the input should be an integer
    return inventory[item_id]

@app.get("/get-item/{item_id}/{name}")
def get_item2(item_id: int, name:str): # define the input should be an integer   
    return inventory[item_id]

@app.get("/get-by-name/{item-id}")
def get_item(item: int, test: int, name:Optional[str] = None ): #in python needs to put mandatory first and optional later
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data": "Not found"}

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists"}
    inventory[item_id] = item
    return inventory[item_id]
    return {}

