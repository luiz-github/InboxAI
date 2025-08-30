from services.openIA_service import OpenIAService
from starlette.responses import JSONResponse

class OpenIAController:
    def __init__(self):
        self.openIA_service = OpenIAService()

    async def get_apiResponse(self, prompt: str):
        response = await self.openIA_service.get_apiResponse(prompt)
        return JSONResponse(status_code=response["stat_code"], content=response)