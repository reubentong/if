from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DOG_API_BASE_URL: str = "https://dogapi.dog/api/v2"
    DOG_API_TIMEOUT_S: int = 10
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
