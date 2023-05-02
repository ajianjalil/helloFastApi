from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Message": "Ajith is a fast learner"}


@app.post("/")
async def post():
    return {"Message": " Message is from post method"}