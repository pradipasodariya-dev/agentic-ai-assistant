import os
from dotenv import load_dotenv

def load_env_keys():
    load_dotenv()
    return {
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
        "WEATHER_API_KEY": os.getenv("WEATHER_API_KEY"),
        "GOOGLE_API_KEY": os.getenv("GOOGLE_API_KEY"),
        "GOOGLE_CX": os.getenv("GOOGLE_CX")
    }
