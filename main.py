from fastapi import Body, FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from pydantic import BaseModel

import os
from fastapi_sqlalchemy import DBSessionMiddleware, db
from dotenv import load_dotenv
load_dotenv(".env")

from schema import Customer,Item
from models import Customer as modelCustomer, Item as modelItem

app = FastAPI(description="""
# This is code for me to refer as well learn fast api
## Thanks to the youtube channel JVP Design for helping me to learn fastapi
""", version="1.0.0")

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])
templates = Jinja2Templates(directory="templates")

# class Customer(BaseModel):
#     name : str | None = None
#     email : str | None = None
#     phone : str | None

# class Item(BaseModel):
#     name : str | None = None
#     price : str | None = None
#     thumbnail : str


app.mount(
    "/static",
    StaticFiles(directory="templates/"),
    name="static",
)

# @app.get("/")
# async def root():
#     return {"Message": "Ajith is a fast learner"}


# @app.post("/")
# async def post():
#     return {"Message": " Message is from post method"}

@app.get("/add-item-page",response_class=HTMLResponse)
async def add_items_page(request: Request):
    return templates.TemplateResponse("add_items.html",{"request":request})

@app.get("/products",response_class=HTMLResponse,tags=["products"])
async def get_dashboard(request: Request):
    return templates.TemplateResponse("products_list.html", {"request": request})


@app.get("/",response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.put("/request_a_call_back")
async def request_a_call_back(request: Request, item:Customer):
    print(" Customer is in the back end",item)
    return {"message":"item created success fully","item":item}

@app.get("/req_call_back_page",response_class=HTMLResponse)
async def req_call_back_page(request: Request):
    return templates.TemplateResponse("form.html",{"request":request})


@app.post('/test_path_param/')
async def test_path_param(q:str | None = "Ajith",item: str | None = Body(default={"name":"Ajith","age":28},description="Ajithkumar Body example")):
    return {"q":q,"item":item}

@app.get("/items")
async def list_of_item():
    items = db.session.query(modelItem).all()
    return items

@app.post("/add-item/", response_model=Item)
def add_book(book: Item):
    db_book = modelItem(title=book.title, rating=book.rating,price=book.price,url=book.url,customer_id=book.customer_id)
    db.session.add(db_book)
    db.session.commit()
    return db_book


@app.post("/add-customer/", response_model=Customer)
def add_author(author: Customer):
    db_author = modelCustomer(name=author.name, mail=author.mail,phone=author.phone)
    db.session.add(db_author)
    db.session.commit()
    return db_author
