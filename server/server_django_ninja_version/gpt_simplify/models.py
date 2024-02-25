from django.db import models

# Create your models here.
class ClickedPaper(models.Model):
    paper_id = models.CharField(max_length=100, unique=True)
    title_en = models.CharField(max_length=400)
    title_ja = models.CharField(max_length=400)
    author = models.JSONField() #特别注意list类型
    categories = models.JSONField()
    published = models.DateTimeField()
    content_en = models.TextField()
    pdf_url = models.URLField()
    content_ja = models.TextField()
    content_plain = models.TextField()
    keywords_list = models.JSONField(default=[])
    # keywords_list = models.TextField() #这样的话，返回的 "Keywords"就变成了 "[]"
    clicked_count = models.IntegerField(default=1)