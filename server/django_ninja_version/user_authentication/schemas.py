from ninja import Schema

class RegisterIn(Schema):
    username: str
    password: str

class LoginIn(Schema):
    username: str
    password: str