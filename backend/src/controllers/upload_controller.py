from services.file_service import FileService
from starlette.responses import JSONResponse

class UploadController:
    def __init__(self):
        self.file_service = FileService()

    async def processFileToPrompt(self, file: any):
        response = await self.file_service.processFileToPrompt(file)
        return JSONResponse(status_code=response["stat_code"], content=response)