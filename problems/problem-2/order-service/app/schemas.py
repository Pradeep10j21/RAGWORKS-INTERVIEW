from pydantic import BaseModel

class OrderBase(BaseModel):
    product_id: int
    user_id: int
    quantity: int

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True
