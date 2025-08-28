from services.file_service import File_service

class UploadController:
    def __init__(self):
        self.file_service = File_service()

    async def processFileToPrompt(self, file: any):
        return await self.file_service.processFileToPrompt(file)
        