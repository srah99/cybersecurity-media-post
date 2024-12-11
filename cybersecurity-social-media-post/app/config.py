from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access API keys and tokens
API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
