from pydantic.v1 import BaseSettings

class Settings(BaseSettings):
    """Settings for the MCP SearxNG integration."""
    searxng_url: str = "http://searxng:8080"

setting = Settings()