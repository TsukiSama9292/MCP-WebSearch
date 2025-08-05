from pydantic.v1 import BaseSettings

class Settings(BaseSettings):
    """Settings for the MCP SearxNG integration."""
    searxng_url: str = "http://192.168.200.102:8080"  # Default SearxNG URL

setting = Settings()