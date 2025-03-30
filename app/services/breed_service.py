import logging

from fastapi import Depends

from app.schemas.schema import BreedsResponse
from app.clients.dogapi import DogAPIClient, get_dog_api_client

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class BreedService:
    def __init__(self, client: DogAPIClient):
        self.client = client

    async def get_breeds(
        self, page: int | None = 1, name: str | None = None
    ) -> BreedsResponse:
        try:
            # I hate this, would prefer to store all breeds from api with caching load (e.g. redis) or
            # an actual DB. However it follows requirements with a presumption we'll extend this.
            all_breeds = (
                await self._fetch_breeds(page=page)
                if page
                else await self._fetch_all_breeds()
            )
            if name:
                all_breeds = _filter_breeds_by_name(all_breeds, name)

            return all_breeds
        except Exception as e:
            logger.error(f"Error fetching breeds: {e}")
            raise

    async def _fetch_breeds(self, page: int | None = 1) -> BreedsResponse:
        response = await self.client.fetch_breeds(page=page)
        breeds = BreedsResponse.model_validate(response)
        return breeds

    async def _fetch_all_breeds(self) -> BreedsResponse:
        breeds = []
        current_page = 1
        while True:
            response = await self.client.fetch_breeds(page=current_page)
            page_data = BreedsResponse.model_validate(response)
            breeds.extend(page_data.data)
            if (
                not page_data.meta
                or not page_data.meta.pagination
                or not page_data.meta.pagination.next
            ):
                break
            current_page += 1

        return BreedsResponse(data=breeds)


def _filter_breeds_by_name(breed_response: BreedsResponse, name: str) -> BreedsResponse:
    filtered = [
        breed
        for breed in breed_response.data
        if name.lower() in breed.attributes.name.lower()
    ]
    return BreedsResponse(data=filtered)


def get_breed_service(
    client: DogAPIClient = Depends(get_dog_api_client),
) -> BreedService:
    return BreedService(client)
