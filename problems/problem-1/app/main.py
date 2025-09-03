from fastapi import FastAPI
from app.database.session import Base, engine
from app.routers import user

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Backend Engineer – Problem 1")

# Include routers
app.include_router(user.router)

@app.get("/")
def root():
    return {"message": "Backend Engineer Problem-1 API running 🚀"}
