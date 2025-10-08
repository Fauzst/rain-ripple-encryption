import pytest
import app.lorenz_system
from app.lorenz_system import LorenzSystem



def test_valid_data_type():
    obj = LorenzSystem()
    result = obj.get_key(10.0, 5.0, 3.0, 10)
    assert isinstance(result, list)
    assert all(isinstance(x, (int, float)) for x in result)

def test_invalid_data_type():
    obj = LorenzSystem()
    with pytest.raises(TypeError):
        obj.get_key("dsfsdfds", 5.0, 3.0, 10)