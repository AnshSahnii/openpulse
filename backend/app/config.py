from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "OpenPulse"
    app_version: str = "1.0.0"
    api_prefix: str = "/api/v1"
    debug: bool = True
    host: str = "127.0.0.1"
    port: int = 8000
    database_url: str = "sqlite:///./openpulse.db"
    jwt_secret: str = "change-me"
    jwt_expire_minutes: int = 1440
    github_token: str = ""
    frontend_url: str = "http://localhost:5173"
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False, extra="ignore")

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
