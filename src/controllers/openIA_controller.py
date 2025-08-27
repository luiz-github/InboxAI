from services.OpenIA_service import OpenIAService

class OpenIAController:
    def __init__(self):
        self.openIA_service = OpenIAService()

    async def get_apiResponse(self, prompt: str):
        response = await self.openIA_service.get_apiResponse(prompt)
        return response