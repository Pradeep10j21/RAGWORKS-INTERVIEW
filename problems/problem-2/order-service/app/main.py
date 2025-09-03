from fastapi import FastAPI
from app.routers import order
from app.database import Base, engine

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Order Service")

app.include_router(order.router)
