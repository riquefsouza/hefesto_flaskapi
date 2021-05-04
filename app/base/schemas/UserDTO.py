import json
from flask import jsonify


class UserDTO:
    id: int
    name: str
    email: str

    def to_json(self):
        #return json.dumps(self.__dict__)
        return jsonify(self.__dict__)
