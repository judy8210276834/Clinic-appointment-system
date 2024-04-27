import os
from dotenv import load_dotenv
from pydantic.v1 import BaseSettings

load_dotenv()

class Settings():
    VERSION: str = "0.110.0"
    TITLE: str = "Clinic appointment system"

    # APIs basic settings
    # base url
    SERVICE_DEBUG: bool = os.getenv('SERVICE_DEBUG',False) == 'True'
    SERVICE_PORT = int(os.getenv('FASTAPI_PORT'))
    WORKER_COUNT = int(os.getenv('WORKER_COUNT'))
    BASE_PATH: str = "/CAS"
    # BASE_PATH: str = "https://ailab.ndmctsgh.edu.tw/aiot_devteam/s/aad353c9ab5a7dc9e95b5/p/969ce1c6"
    BASE_PREFIX: str = "/api/v1"
    
basicSettings = Settings()

class AuthSettings():

    # authentication
    ALGORITHM: str = "HS256"
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7
    REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 14
    
    # token url
    OAUTH_PREFIX: str = "/api/v1"

authSettings = AuthSettings()

class DatabaseSettings(BaseSettings):
    DATABASE_PORT: int
    POSTGRES_HOST: str
    POSTGRES_HOSTNAME: str

    AUTH_DB_USER: str
    AUTH_DB_PASSWORD: str
    AUTH_DB_NAME: str
    
    CLINIC_APPOINTMENT_SYSTEM_DB_USER: str
    CLINIC_APPOINTMENT_SYSTEM_DB_PASSWORD: str
    CLINIC_APPOINTMENT_SYSTEM_DB_NAME: str
    
    class Config:
        env_file = 'app/configs/.env'

dbSettings = DatabaseSettings()
