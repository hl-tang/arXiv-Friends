from ninja import Schema, ModelSchema
from gpt_simplify.models import Paper

class PaperOut(ModelSchema):
    class Meta:
        model = Paper
        fields = "__all__"
