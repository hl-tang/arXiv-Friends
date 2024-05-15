from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from gpt_simplify.models import ClickedPaper

# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f"{self.username}"

class TouristSession(models.Model):
    free_access_token = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    expire = models.DateTimeField()
    used_simplify_api_count = models.IntegerField(default=1)

class UserLikePaper(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    paper_id = models.ForeignKey(ClickedPaper, on_delete=models.CASCADE)

class UserBrowsePaperHistory(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    paper_id = models.ForeignKey(ClickedPaper, on_delete=models.CASCADE)
