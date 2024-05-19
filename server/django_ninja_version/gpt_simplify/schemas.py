from ninja import Schema
from datetime import datetime

class GPTSimplifyIn(Schema):
    paper_id: str
    content_en: str
