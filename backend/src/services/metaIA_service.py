import http
import json
import os
import re
from src.helpers.generic_helper import APIResponse, api_response
from src.helpers.preprocess_helper import preprocess_text
from src.helpers.prompt_helper import prompt_template
from src.dto.promptRequest_dto import PromptRequest
from dotenv import load_dotenv
import requests

load_dotenv()

class MetaIAService:
    def __init__(self):
        self.API_KEY = os.getenv("API_KEY")
        self.BASE_URL = os.getenv("BASE_URL")

    async def get_apiResponse(self, prompt: PromptRequest) -> APIResponse:
        try:
            promptTemplate = prompt_template(preprocess_text(prompt))
            headers = {
                "Content-Type": "application/json",
                "X-goog-api-key": self.API_KEY
            }
            body = {
                "contents": [
                    {
                        "parts": [
                            {
                                "text": promptTemplate
                            }
                        ]
                    }
                ]
            } 
            response = (requests.post(self.BASE_URL, headers=headers, json=body)).json()
            raw_text = response["candidates"][0]["content"]["parts"][0]["text"]
            response = json.loads(re.sub(r"```json\n([\s\S]+?)\n```", r"\1", raw_text).strip())
            return api_response(http.HTTPStatus.OK, "Success", response)
        except Exception as e:
            return api_response(http.HTTPStatus.BAD_REQUEST, str(e))