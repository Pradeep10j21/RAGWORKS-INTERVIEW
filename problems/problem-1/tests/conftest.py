# tests/conftest.py
import pytest
from app.database import Base, engine

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    # Creates all tables before tests
    Base.metadata.create_all(bind=engine)
