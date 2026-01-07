import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME = 'Car Price API'
    API_KEY = os.getenv('API_KEY', 'demo-key')  # here the first parameter points to .env file and the second parameter 
                                                # is used when first parameter fails get the value from the .env file
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'secret')
    JWT_ALGORITHM = 'HS256'
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')
    MODEL_PATH = 'app/models/model.joblib'



settings=Settings()
