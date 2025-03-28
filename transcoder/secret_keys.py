from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class SecretKeys(BaseSettings):
    REGION_NAME: str = "us-east-1"
