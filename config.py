from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

DATABASE = {
     'name': os.getenv('DATABASE_NAME'),
     'user': os.getenv('DATABASE_USER'),
     'password': os.getenv('DATABASE_PASSWORD'),
     'host': os.getenv('DATABASE_HOST'),
     'port': os.getenv('DATABASE_PORT')
}
