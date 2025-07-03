from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "SheetMind"
    upload_dir: str = "uploads"

settings = Settings()
