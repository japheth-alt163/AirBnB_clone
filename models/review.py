from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review class inherits from BaseModel.

    Public class attributes:
    - place_id: string (empty string by default)
    - user_id: string (empty string by default)
    - text: string (empty string by default)
    """
    place_id = ""
    user_id = ""
    text = "
