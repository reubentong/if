from typing import Any
from unittest.mock import AsyncMock, patch

import pytest

from app.services.clients.dogapi import DogAPIClient


@pytest.mark.asyncio
async def test_fetch_breeds(
    dog_api: DogAPIClient, mock_breeds_response: dict[str, Any]
) -> None:
    with patch.object(
        dog_api,
        "fetch_breeds",
        new_callable=AsyncMock,
        return_value=mock_breeds_response,
    ):
        assert await dog_api.fetch_breeds() == mock_breeds_response
