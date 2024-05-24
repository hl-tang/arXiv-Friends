from ninja import Schema, ModelSchema
from gpt_simplify.models import Paper

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

class LikePaperOut(ModelSchema):
    class Meta:
        model = Paper
        fields = ['paper_id', 'title_en', 'title_ja', 'authors', \
                  'categories', 'published', 'content_en', 'pdf_url']