import os
from dotenv import load_dotenv


class EnvLoader:
    def __init__(self, path=".env"):
        load_dotenv()

    @staticmethod
    def get_url():
        return os.getenv("API_URL")

    @staticmethod
    def get_api_key():
        return os.getenv("API_KEY")

    @staticmethod
    def get_model_id():
        return os.getenv("MODEL_ID")