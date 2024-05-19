from ninja import Schema, ModelSchema
from gpt_simplify.models import Paper

class PaperOut(ModelSchema):
    class Meta:
        model = Paper
        # 这样定义fields返回的json的key名就和数据库的字段名一样
        fields = ['paper_id', 'title_en', 'title_ja', 'authors', \
                  'categories', 'published', 'content_en', 'pdf_url', 'clicked_count']
