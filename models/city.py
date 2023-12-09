from models.base_model import BaseModel


class City(BaseModel):
    """
    City class inherits from BaseModel.

    Public class attributes:
    - state_id: string (empty string by default)
    - name: string (empty string by default)
    """
    state_id = ""
    name = ""
