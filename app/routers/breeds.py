import logging

from fastapi import APIRouter

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
router = APIRouter(prefix="/breeds", tags=["Breeds"])
