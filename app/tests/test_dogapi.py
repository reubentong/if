import pytest


@pytest.mark.asyncio
async def test_fetch_breeds(mock_dog_api):
    mock_dog_api.fetch_breeds.return_value = {"breeds": ["Labrador", "Poodle"]}

    result = await mock_dog_api.fetch_breeds()

    assert isinstance(result, dict)
    assert "breeds" in result
    assert result["breeds"] == ["Labrador", "Poodle"]
