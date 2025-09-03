import asyncio
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncpg
import aioredis

# ------------------------------
# Configuration
# ------------------------------
DATABASE_URL = "postgresql://postgres:mysecretpassword@postgres_db:5432/mydb"
REDIS_URL = "redis://redis_cache:6379"

# ------------------------------
# Pydantic Models
# ------------------------------
class User(BaseModel):
    id: int | None = None
    name: str
    email: str

# ------------------------------
# FastAPI App
# ------------------------------
app = FastAPI(title="Backend Engineer Assessment")

# ------------------------------
# Global Pools
# ------------------------------
db_pool: asyncpg.pool.Pool | None = None
redis: aioredis.Redis | None = None

# ------------------------------
# Startup & Shutdown Events
# ------------------------------
@app.on_event("startup")
async def startup():
    global db_pool, redis
    # PostgreSQL
    db_pool = await asyncpg.create_pool(DATABASE_URL)
    # Redis
    redis = await aioredis.from_url(REDIS_URL, encoding="utf-8", decode_responses=True)
    # Create table if not exists
    async with db_pool.acquire() as conn:
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        """)

@app.on_event("shutdown")
async def shutdown():
    global db_pool, redis
    if db_pool:
        await db_pool.close()
    if redis:
        await redis.close()

# ------------------------------
# Routes
# ------------------------------
@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/users", response_model=User)
async def create_user(user: User):
    query = "INSERT INTO users (name, email) VALUES ($1, $2) RETURNING id, name, email"
    async with db_pool.acquire() as conn:
        try:
            record = await conn.fetchrow(query, user.name, user.email)
            # Optionally cache in Redis
            await redis.set(f"user:{record['id']}", f"{record['name']}|{record['email']}")
            return User(**record)
        except asyncpg.UniqueViolationError:
            raise HTTPException(status_code=400, detail="Email already exists")

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    # Check Redis cache first
    cached = await redis.get(f"user:{user_id}")
    if cached:
        name, email = cached.split("|")
        return User(id=user_id, name=name, email=email)
    
    query = "SELECT id, name, email FROM users WHERE id=$1"
    async with db_pool.acquire() as conn:
        record = await conn.fetchrow(query, user_id)
        if not record:
            raise HTTPException(status_code=404, detail="User not found")
        # Cache in Redis
        await redis.set(f"user:{record['id']}", f"{record['name']}|{record['email']}")
        return User(**record)

@app.get("/users", response_model=List[User])
async def list_users():
    query = "SELECT id, name, email FROM users"
    async with db_pool.acquire() as conn:
        records = await conn.fetch(query)
        return [User(**r) for r in records]
