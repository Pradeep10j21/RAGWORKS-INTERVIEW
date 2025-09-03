from sqlalchemy import Column, Integer
from app.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, index=True)
    user_id = Column(Integer, index=True)
    quantity = Column(Integer)
