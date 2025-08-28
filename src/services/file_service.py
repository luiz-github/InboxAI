import http
from services.openIA_service import OpenIAService
from helpers.generic_helper import APIResponse, api_response
import pypdf
from io import BytesIO

class File_service:
    def __init__(self):
        self.openIA_service = OpenIAService()

    async def processFileToPrompt(self, file) -> APIResponse:
        if ".txt" in file.filename:
            try:
                content = await file.read()
                text = content.decode('utf-8')
                response = await self.openIA_service.get_apiResponse(text)
                return api_response(http.HTTPStatus.OK, "Read successfully", response["data"])
            except Exception as e:
                return api_response(http.HTTPStatus.BAD_REQUEST, str(e))
            
        elif ".pdf" in file.filename:
            try:
                contents = await file.read()
                pdf_file = BytesIO(contents)
                reader = pypdf.PdfReader(pdf_file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() or ""

                response = await self.openIA_service.get_apiResponse(text)
                return api_response(http.HTTPStatus.OK, "Read successfully", response["data"])
            except Exception as e:
                return api_response(http.HTTPStatus.BAD_REQUEST, str(e))
        return api_response(http.HTTPStatus.BAD_REQUEST, "File extension is not supported")