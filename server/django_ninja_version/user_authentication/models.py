from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from gpt_simplify.models import Paper

# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f"{self.username}"


class TouristSession(models.Model):
    free_access_token = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    expire = models.DateTimeField()
    used_simplify_api_count = models.IntegerField(default=1)


class UserLikePaper(models.Model):
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # paper_id = models.ForeignKey(Paper, on_delete=models.CASCADE)
    # 外键加_id的话，数据库字段变成了user_id_id
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'paper'], name='user_like_paper')
        ]


class UserBrowsePaperHistory(models.Model):
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # paper_id = models.ForeignKey(Paper, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'paper'], name='user_browser_paper_history')
        ]
