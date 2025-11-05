import pytest
from app.env_loader import EnvLoader
from app.ai_model import AIModel

def test_no_path():
    with pytest.raises(FileNotFoundError):
        ai = AIModel("wrong file path")
        ai.get_model_result()

def test_number_path():
    with pytest.raises(FileNotFoundError):
        ai = AIModel(1231)
        ai.get_model_result()