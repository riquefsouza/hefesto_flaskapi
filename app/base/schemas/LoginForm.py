from typing import Dict

class LoginForm:
    login: str
    password: str

    def __init__(self, loginForm: Dict):
        self.login=loginForm["login"]
        self.password=loginForm["password"]
