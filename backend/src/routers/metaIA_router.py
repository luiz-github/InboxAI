from fastapi import APIRouter
from src.controllers.metaIA_controller import MetaIAController
from src.dto.promptRequest_dto import PromptRequest

router = APIRouter()
openIA_controller = MetaIAController()

@router.post("/generateEmailResponse")
async def generate_emailResponse(request: PromptRequest):
    return await openIA_controller.get_apiResponse(prompt=request.prompt)
