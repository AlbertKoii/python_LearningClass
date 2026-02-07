# pip install -U google-genai 
from dotenv import load_dotenv
import os 
from google import genai

load_dotenv()

url = os.getenv("geminiKey")
prompts = ""
client = genai.Client(api_key = url)

def conversation (): 
    client.models.generate_content (
        model = "Gemini 2.5 Flash-Lite",
        content = prompts,
        config={
            "system_instruction": "你是一個專業的技術顧問，請簡短回答。"
        }
    )
    
    