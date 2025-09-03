# problems/problem-3/tests/test_performance.py
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_users_endpoints():
    async with AsyncClient(app=app, base_url="http://test") as client:
        r1 = await client.get("/users_slow")
        r2 = await client.get("/users_fast")
        assert r1.status_code == 200
        assert r2.status_code == 200
