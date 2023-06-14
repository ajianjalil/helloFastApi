from fastapi import Body, FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class Customer(BaseModel):
    name : str | None = None
    email : str | None = None
    phone : str | None

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

@app.get("/home")
async def get():
    ret='''
    <html>
    <body>
    <h2>Home!</h2>
    </body>
    </html>
    '''
    return HTMLResponse(content=ret)

@app.get("/products",response_class=HTMLResponse)
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
