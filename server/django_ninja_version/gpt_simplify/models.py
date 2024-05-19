from django.db import models

# Create your models here.
class Paper(models.Model):
    paper_id = models.CharField(max_length=100, primary_key=True)
    title_en = models.CharField(max_length=400)
    title_ja = models.CharField(max_length=400)
    authors = models.JSONField() #特别注意list类型
    categories = models.JSONField()
    published = models.DateTimeField()
    content_en = models.TextField()
    pdf_url = models.URLField()
    clicked_count = models.IntegerField(default=0)

class SimplifyAbstract(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, primary_key=True)
    # 实际数据库里的字段叫paper_id,好像外键的话迁移时orm会自动在后面加上_id或者是用的关联表的主键名?
    # 反正orm的时候用paper_id，即使此处定义是paper字段
    content_ja = models.TextField()
    content_plain = models.TextField()

class Keywords(models.Model):
    paper = models.ForeignKey(SimplifyAbstract, on_delete=models.CASCADE, primary_key=True)
    keywords_list = models.JSONField(default=[])
    # keywords_list = models.TextField() #这样的话，返回的 "Keywords"就变成了 "[]"
