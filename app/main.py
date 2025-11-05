from app.startup_message import startup_message
from app.ai_model import AIModel
from parameters_getter import ParametersGetter
from lorenz_system import LorenzSystem
from image_processor import ImageProcessor
import time

startup_message()
inp = input("Please enter your input: ")


ai_model = AIModel(inp)
params = ParametersGetter(ai_model.get_model_result())
params.get_params()