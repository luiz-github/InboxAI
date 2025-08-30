import http

from fastapi import UploadFile
from services.openIA_service import OpenIAService
from helpers.generic_helper import APIResponse, api_response
import pypdf
from io import BytesIO


class FileService:
    def __init__(self):
        self.openIA_service = OpenIAService()
        self.handlers = {
            ".txt": self._process_txt,
            ".pdf": self._process_pdf,
        }

    async def processFileToPrompt(self, file: UploadFile) -> APIResponse:
        try:
            extension = file.filename.lower()

            for ext, handler in self.handlers.items():
                if extension.endswith(ext):
                    text = await handler(file)
                    return await self._process_with_gemini(text)

            return api_response(http.HTTPStatus.BAD_REQUEST, "File extension is not supported")

        except Exception as e:
            return api_response(http.HTTPStatus.BAD_REQUEST, f"Unexpected error: {str(e)}")

    async def _process_txt(self, file: UploadFile) -> str:
        content = await file.read()
        return content.decode("utf-8")

    async def _process_pdf(self, file: UploadFile) -> str:
        contents = await file.read()
        pdf_file = BytesIO(contents)
        reader = pypdf.PdfReader(pdf_file)
        return " ".join(page.extract_text() or "" for page in reader.pages)

    async def _process_with_gemini(self, text: str) -> APIResponse:
        response = await self.openIA_service.get_apiResponse(text)
        return api_response(http.HTTPStatus.OK, "Read successfully", response.get("data"))