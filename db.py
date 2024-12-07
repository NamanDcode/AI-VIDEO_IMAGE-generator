from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = "sqlite:///generated_content.db"  # Change this to your preferred database URL

# Create an engine and session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the tables in the database
def init_db():
    Base.metadata.create_all(bind=engine)
