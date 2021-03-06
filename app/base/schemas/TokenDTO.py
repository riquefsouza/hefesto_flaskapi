import json
from flask import jsonify


class TokenDTO:
    token: str
    tipo: str

    def __init__(self, token: str, tipo: str):
        self.token = token
        self.tipo = tipo

    def to_json(self):
        #return json.dumps(self.__dict__)
        return jsonify(self.__dict__)
