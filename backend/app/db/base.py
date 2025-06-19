from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL

# Create a SQLAlchemy engine using the DATABASE_URL
engine = create_engine(DATABASE_URL)

# Create a SessionLocal class using the sessionmaker function
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for declarative base model definitions
Base = declarative_base()

# Define a dependency function for getting a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()