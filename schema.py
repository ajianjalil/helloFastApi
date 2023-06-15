from pydantic import BaseModel

class Item(BaseModel):
    title : str
    rating : int
    price : int
    url : str
    customer_id: int
    class Config:
        orm_mode = True


class Customer(BaseModel):
    name : str
    mail : str
    phone :  str

    class Config:
        orm_mode = True