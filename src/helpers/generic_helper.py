from typing import Any, Optional

class APIResponse:
    stat_code: int
    message: str
    data: Optional[Any] = None

def api_response(code: int, message: str, data: Optional[Any] = None)-> APIResponse:
    if data is None:
        return {
            "stat_code": code,
            "message": message,
        }
    else:
        return {
            "stat_code": code,
            "message": message,
            "data": data
        }