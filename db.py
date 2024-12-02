from flask import g # `g` stores connection info for the request
from app import db

# Get database connection (SQLAlchemy manages this)
def get_db_connection():
    return db
    
