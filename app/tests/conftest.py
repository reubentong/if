from unittest.mock import AsyncMock

import pytest

from app.config import Settings
from app.services.clients import dogapi


@pytest.fixture
def settings():
    return Settings(DOG_API_BASE_URL="https://mockapi.test", DOG_API_TIMEOUT_S=10)


@pytest.fixture
def mock_dog_api(settings):
    api = dogapi.DogAPI(settings)
    api.fetch_breeds = AsyncMock()
    return api
