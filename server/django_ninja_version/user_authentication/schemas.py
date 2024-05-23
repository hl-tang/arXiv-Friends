from ninja import Schema

class RegisterIn(Schema):
    username: str
    password: str

class LoginIn(Schema):
    username: str
    password: str

class NotesPostIn(Schema):
    paper_id: str
    notes: str

class NotesGetOut(Schema):
    notes: str