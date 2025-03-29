from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DOG_API_BASE_URL: str = "https://myapi.co.uk"
    DOG_API_TIMEOUT_S: int = 10

settings = Settings()
