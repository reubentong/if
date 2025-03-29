from typing import Any

import httpx

from app.config import Settings


class DogAPI:
    def __init__(self, settings: Settings):
        self.client = httpx.AsyncClient(
            base_url=settings.DOG_API_BASE_URL,
            timeout=settings.DOG_API_TIMEOUT_S,
        )

    async def fetch_breeds(self) -> dict[str, Any]:
        try:
            response = await self.client.get("/breeds")
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise httpx.HTTPStatusError(
                f"API error: {e.response.status_code} {e.response.text}",
                request=e.request,
                response=e.response,
            )
