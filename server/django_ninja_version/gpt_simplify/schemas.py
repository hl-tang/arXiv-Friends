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
