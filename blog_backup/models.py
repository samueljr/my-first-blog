from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.TextField(default="")
    party = models.CharField(max_length=1)
    state_code = models.CharField(max_length=2)
    np_score = models.CharField(max_length=7)
    id = models.IntegerField(primary_key=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    text = models.CharField(max_length=1)
    title = models.CharField(max_length=1)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

