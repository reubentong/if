import pytest

from app.schemas.schema import BreedsResponse
from app.services.breed_service import BreedService


@pytest.mark.asyncio
async def test_get_breeds_single_page(
    breed_service: BreedService, breeds: BreedsResponse
) -> None:
    response = await breed_service.get_breeds(page=1)
    assert isinstance(response, BreedsResponse)
    assert len(response.data) == 1


@pytest.mark.asyncio
async def test_get_all_breeds(
    breed_service: BreedService, breeds: BreedsResponse
) -> None:
    response = await breed_service.get_breeds()
    assert isinstance(response, BreedsResponse)
    assert len(response.data) == 1


@pytest.mark.asyncio
async def test_filter_by_name(
    breed_service: BreedService, breeds: BreedsResponse
) -> None:
    response = await breed_service.get_breeds(name="Golden Doodle")
    assert isinstance(response, BreedsResponse)
    assert len(response.data) == 1


@pytest.mark.asyncio
async def test_filter_by_name(
    breed_service: BreedService, breeds: BreedsResponse
) -> None:
    response = await breed_service.get_breeds(name="Labrador")
    assert isinstance(response, BreedsResponse)
    assert len(response.data) == 0
