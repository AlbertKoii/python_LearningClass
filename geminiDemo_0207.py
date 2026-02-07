# pip install -U google-genai 
from dotenv import load_dotenv
import os 
from google import genai

load_dotenv()
url = os.getenv("geminiKey")

