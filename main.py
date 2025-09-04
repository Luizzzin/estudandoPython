import os 
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

CHAVE_API_KEY = os.getenv("GEMINI_API_KEY")