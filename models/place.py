from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class inherits from BaseModel.

    Public class attributes:
    - city_id: string (empty string by default)
    - user_id: string (empty string by default)
    - name: string (empty string by default)
    - description: string (empty string by default)
    - number_rooms: integer (0 by default)
    - number_bathrooms: integer (0 by default)
    - max_guest: integer (0 by default)
    - price_by_night: integer (0 by default)
    - latitude: float (0.0 by default)
    - longitude: float (0.0 by default)
    - amenity_ids: list of strings (empty list by default)
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
