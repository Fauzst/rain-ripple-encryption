#========== HEADER ===================================================================
"""
Document: env_loader.py
Function: Module for getting information on the .env file
Author: PURA, Joshua Elijah L.
Date Created: October 6, 2025
Date Updated: October 13, 2025
Version: 0.0.2
"""
#======================================================================================

#=========== LIBRARIES ================================================================
import os
from dotenv import load_dotenv
#======================================================================================

#=========== CLASS ====================================================================
class EnvLoader:
    def __init__(self, path=".env"):

        load_dotenv()

    @staticmethod
    def get_url():
        """
        Function: get_url
        Description: This public function uses os and dotenv libraries to read
                     the .env file and return the API's url.
        Arguments:
            none.
        Returns:
            API_URL (str): The API URL.
        Raises:
            none
        """
        return os.getenv("API_URL")

    @staticmethod
    def get_api_key():
        """
        Function: get_api_key
        Description: This public function uses os and dotenv libraries to read
                     the .env file and return the API's key.
        Arguments:
            none.
        Returns:
            API_KEY (str): The API KEY.
        Raises:
            none
        """
        return os.getenv("API_KEY")

    @staticmethod
    def get_model_id():
        """
        Function: get_api_id
        Description: This public function uses os and dotenv libraries to read
                     the .env file and return the API's model id.
        Arguments:
            none.
        Returns:
            MODEL_ID (str): The API model ID.
        Raises:
            none
        """
        return os.getenv("MODEL_ID")

#========= END OF SOURCE CODE ==========================================================