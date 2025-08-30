from services.metaIA_service import MetaIAService
from starlette.responses import JSONResponse

class MetaIAController:
    def __init__(self):
        self.metaIA_service = MetaIAService()

    async def get_apiResponse(self, prompt: str):
        response = await self.metaIA_service.get_apiResponse(prompt)
        return JSONResponse(status_code=response["stat_code"], content=response)