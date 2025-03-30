import logging

from fastapi import Depends

from app.schemas.schema import BreedsResponse, Breed
from app.services.clients.dogapi import DogAPIClient, get_dog_api_client

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class BreedService:
    def __init__(self, client: DogAPIClient):
        self.client = client

    async def get_breeds(self, page: int | None = 1) -> BreedsResponse:
        try:
            all_breeds = await self._fetch_all_breeds(page=page)
            return all_breeds
        except Exception as e:
            logger.error(f"Error fetching breeds: {e}")
            raise

    async def _fetch_all_breeds(self, page: int | None) -> BreedsResponse:
        response = await self.client.fetch_breeds(page=page)
        breeds = BreedsResponse.model_validate(response)
        return breeds


def get_breed_service(
    client: DogAPIClient = Depends(get_dog_api_client),
) -> BreedService:
    return BreedService(client)
