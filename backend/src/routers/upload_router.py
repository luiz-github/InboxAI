from controllers.upload_controller import UploadController
from fastapi import APIRouter, UploadFile

router = APIRouter()
uploadController = UploadController()

@router.post("/processFileToPrompt")
async def upload_file(file: UploadFile):
    return await uploadController.processFileToPrompt(file)