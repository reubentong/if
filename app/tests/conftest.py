import uuid
from unittest.mock import AsyncMock

import pytest

from app.clients.dogapi import DogAPIClient
from app.config import Settings
from app.schemas.schema import (
    BreedsResponse,
    Breed,
    Meta,
    Pagination,
    BreedAttributes,
    BreedLifeSpan,
    BreedWeight,
    BreedRelationships,
    GroupRelationship,
    GroupData,
)
from app.services.breed_service import BreedService


@pytest.fixture
def settings() -> Settings:
    return Settings(DOG_API_BASE_URL="https://dogapi.dog/api/v2", DOG_API_TIMEOUT_S=10)


@pytest.fixture
def mock_dog_api(breeds: BreedsResponse) -> AsyncMock:
    mock_client = AsyncMock()
    mock_client.fetch_breeds.return_value = breeds.model_dump()
    return mock_client


@pytest.fixture
def breed_service(mock_dog_api: DogAPIClient) -> BreedService:
    return BreedService(mock_dog_api)


@pytest.fixture
def breeds() -> BreedsResponse:
    return BreedsResponse(
        data=[
            Breed(
                id=uuid.uuid4(),
                type="breed",
                attributes=BreedAttributes(
                    name="Golden Doodle",
                    description="Reuben's Dog",
                    life=BreedLifeSpan(max=9999, min=100),
                    male_weight=BreedWeight(max=75, min=65),
                    female_weight=BreedWeight(max=65, min=55),
                    hypoallergenic=False,
                ),
                relationships=BreedRelationships(
                    group=GroupRelationship(
                        data=GroupData(id=uuid.uuid4(), type="group")
                    )
                ),
            ),
        ],
        meta=Meta(pagination=Pagination(next=None)),
    )
