from ninja import Schema
from datetime import datetime

class GPTSimplifyIn(Schema):
    Paper_ID: str
    Title_En: str
    Title_Ja: str
    Authors: list
    Categories: list
    Published: datetime
    Content_En: str
    Pdf_url: str

class KeyWordSchema(Schema):
    Keyword: str
    Description: str

class GPTSimplifyOut(Schema):
    Paper_ID: str
    Content_En: str
    Content_Ja: str
    Content_plain: str
    Keywords: list[KeyWordSchema]
    clicked_count: int
