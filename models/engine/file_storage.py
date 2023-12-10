import json
import sys

class FileStorage:
    """
    FileStorage class for serializing instances to a JSON file and deserializing JSON file to instances.
    """
    _file_path = "file.json"
    _objects = {}

    @classmethod
    def all(cls):
        """
        Return the dictionary _objects.
        """
        return cls._objects

    @classmethod
    def new(cls, obj):
        """
        Set in _objects the obj with key <obj class name>.id.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        cls._objects[key] = obj

    @classmethod
    def save(cls):
        """
        Serialize _objects to the JSON file (path: _file_path).
        """
        with open(cls._file_path, 'w', encoding='utf-8') as file:
            obj_dict = {key: obj.to_dict() for key, obj in cls._objects.items()}
            json.dump(obj_dict, file)

    @classmethod
    def reload(cls):
        """
        Deserialize the JSON file to _objects (only if the JSON file (_file_path) exists).
        """
        try:
            with open(cls._file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                for key, obj in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    obj_class = getattr(sys.modules[__name__], class_name)
                    cls._objects[key] = obj_class(**obj)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            # Handle the error (e.g., log it or raise a more specific exception)
            pass
