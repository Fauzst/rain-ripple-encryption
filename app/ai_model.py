import json
from inference_sdk import InferenceHTTPClient
from app.env_loader import EnvLoader
import os

class AIModel:
    def __init__(self, image_path):
        env = EnvLoader()
        self.image_path = image_path
        self.api_url = env.get_url()
        self.api_key = env.get_api_key()
        self.model_id= env.get_model_id()


    def __generate_model_result(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_dir, self.image_path)

        CLIENT = InferenceHTTPClient(
            api_url=self.api_url,
            api_key=self.api_key
        )

        return CLIENT.infer(image_path, model_id=self.model_id)

    def get_model_result(self):
        try:
            return self.__generate_model_result()
        except:
            print("No image found in that path!")
            raise FileNotFoundError

