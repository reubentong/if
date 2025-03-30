import json
from typing import Any
from unittest.mock import AsyncMock, patch

import pytest

from app.clients.dogapi import DogAPIClient


@pytest.fixture
def mock_breeds_response() -> dict[str, Any]:
    with open("app/tests/fixtures/breeds.json", "r") as f:
        json_fixture: dict[str, Any] = json.load(f)
        return json_fixture


@pytest.mark.asyncio
async def test_fetch_breeds(
    mock_dog_api: DogAPIClient, mock_breeds_response: dict[str, Any]
) -> None:
    with patch.object(
        mock_dog_api,
        "fetch_breeds",
        new_callable=AsyncMock,
        return_value=mock_breeds_response,
    ):
        assert await mock_dog_api.fetch_breeds() == mock_breeds_response
