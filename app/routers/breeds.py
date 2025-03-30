import logging

from fastapi import APIRouter, Depends, HTTPException

from app.schemas.schema import BreedsResponse
from app.services.breed_service import BreedService, get_breed_service

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
router = APIRouter(prefix="", tags=["Breeds"])


@router.get("/breeds", response_model=BreedsResponse)
async def get_breeds(
    service: BreedService = Depends(get_breed_service),
    page: int | None = None,
    name: str | None = None,
) -> BreedsResponse:
    try:
        return await service.get_breeds(page=page, name=name)
    except Exception as e:
        logger.error(f"Error fetching breeds: {e}")
        raise HTTPException(status_code=500, detail="Error fetching breeds")
