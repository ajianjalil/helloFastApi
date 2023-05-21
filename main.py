from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()
templates = Jinja2Templates(directory="templates")

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