import os
from dotenv import load_dotenv
import requests
from helpers.preprocess_text import preprocess_text

load_dotenv(dotenv_path="dotenv/.env")

class OpenIAService:
    def __init__(self):
        self.API_KEY = os.getenv("API_KEY")
        self.BASE_URL = os.getenv("BASE_URL")

    async def get_apiResponse(self, prompt):
        text = preprocess_text(prompt)
        headers = {
            "Content-Type": "application/json",
            "X-goog-api-key": self.API_KEY
        }
        body = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": text
                        }
                    ]
                }
            ]
        } 
        response = requests.post(self.BASE_URL, headers=headers, json=body) 
        return response.json()