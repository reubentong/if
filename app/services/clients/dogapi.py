from typing import Any

import httpx

from app.config import Settings


class DogAPIClient:
    def __init__(self, settings: Settings):
        self.client = httpx.AsyncClient(
            base_url=settings.DOG_API_BASE_URL,
            timeout=settings.DOG_API_TIMEOUT_S,
        )

    async def fetch_breeds(self, page: int | None = 1) -> dict[str, Any]:
        try:
            params = {}
            if page:
                params["page[number]"] = page
            response = await self.client.get("/breeds", params=params)
            response.raise_for_status()
            result: dict[str, Any] = response.json()
            return result
        except httpx.HTTPStatusError as e:
            raise httpx.HTTPStatusError(
                f"Dog API error: {e.response.status_code} {e.response.text}",
                request=e.request,
                response=e.response,
            )


def get_dog_api_client() -> DogAPIClient:
    settings = Settings()
    return DogAPIClient(settings)
