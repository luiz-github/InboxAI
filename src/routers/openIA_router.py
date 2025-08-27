from fastapi import APIRouter
from controllers.openIA_controller import OpenIAController
from pydantic import BaseModel
from dto.promptRequest_dto import PromptRequest

router = APIRouter()
openIA_controller = OpenIAController()

@router.post("/generateEmailResponse")
async def generate_emailResponse(request: PromptRequest):
    return await openIA_controller.get_apiResponse(prompt=request.prompt)
