from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import httpx
import os

app = FastAPI(title="API Gateway")

USER_SERVICE = os.getenv("USER_SERVICE", "http://user-service:8000")
PRODUCT_SERVICE = os.getenv("PRODUCT_SERVICE", "http://product-service:8001")
ORDER_SERVICE = os.getenv("ORDER_SERVICE", "http://order-service:8002")

@app.get("/")
def root():
    return {"message": "API Gateway running"}

@app.api_route("/users/{path:path}", methods=["GET", "POST"])
async def proxy_user(path: str, request: httpx.Request):
    async with httpx.AsyncClient() as client:
        resp = await client.request(request.method, f"{USER_SERVICE}/users/{path}", json=await request.json())
        return resp.json()

@app.api_route("/products/{path:path}", methods=["GET", "POST"])
async def proxy_product(path: str, request: httpx.Request):
    async with httpx.AsyncClient() as client:
        resp = await client.request(request.method, f"{PRODUCT_SERVICE}/products/{path}", json=await request.json())
        return resp.json()

@app.api_route("/orders/{path:path}", methods=["GET", "POST"])
async def proxy_order(path: str, request: httpx.Request):
    async with httpx.AsyncClient() as client:
        resp = await client.request(request.method, f"{ORDER_SERVICE}/orders/{path}", json=await request.json())
        return resp.json()
