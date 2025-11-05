#============ HEADER =================================================
"""
Document: ai_model.py
Function: Module for integrating Yolo V8 A.I. model in the system.
Author: PURA, Joshua Elijah L.
Date Created: October 6, 2025
Date Updated: October 13, 2025
Version: 0.0.2
"""
#======================================================================

#============= LIBRARIES ==============================================
from inference_sdk import InferenceHTTPClient
from app.env_loader import EnvLoader
import os
#======================================================================

#============= CLASS ==================================================
class AIModel:
    def __init__(self, image_path):
        env = EnvLoader()
        self.image_path = image_path
        self.api_url = env.get_url()
        self.api_key = env.get_api_key()
        self.model_id= env.get_model_id()


    def __generate_model_result(self):
        """
        Function: __generate_model_result
        Description: This private function process the integration of
                     connecting to RoboFlow to use the trained Yolo V8 model
                     in it.
        Arguments:
            none.
        Returns:
            parameters (str): A dictionary of parameters get by detecting rain
                              ripples.
        Raises:
            none
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_dir, self.image_path)
        CLIENT = InferenceHTTPClient(
            api_url=self.api_url,
            api_key=self.api_key
        )

        return CLIENT.infer(image_path, model_id=self.model_id)

    def get_model_result(self):
        """
        Function: get_model_result
        Description: This public function is just created to serve the result
                     from the private function __generate_model_result. This
                     ensures that it will not expose any critical information.
        Arguments:
            none.
        Returns:
            parameters (str): A dictionary of parameters got by detecting rain
                              ripples.
        Raises:
            FileNotFoundError: When the url fed in the infer was not detected,
                               it will return a FileNotFoundError.
        """
        try:
            return self.__generate_model_result()
        except:
            print("No image found in that path!")
            raise FileNotFoundError

#==================== END OF SOURCE CODE =======================================================
