# create_tables.py
from app.database.session import Base, engine
import app.models.user  # make sure all your models are imported

# Create all tables
Base.metadata.create_all(bind=engine)
print("Tables created successfully!")
