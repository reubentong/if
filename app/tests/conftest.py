import json
from typing import Any, Dict

import pytest

from app.config import Settings
from app.services.clients.dogapi import DogAPIClient


@pytest.fixture
def settings() -> Settings:
    return Settings(DOG_API_BASE_URL="https://dogapi.dog/api/v2", DOG_API_TIMEOUT_S=10)


@pytest.fixture
def dog_api(settings: Settings) -> DogAPIClient:
    return DogAPIClient(settings=settings)


@pytest.fixture
def mock_breeds_response() -> dict[str, Any]:
    with open("app/tests/fixtures/breeds.json", "r") as f:
        json_fixture: dict[str, Any] = json.load(f)
        return json_fixture
