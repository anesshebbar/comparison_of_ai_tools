
from django.db import models
from django.contrib.auth.models import User


class Chatbot(models.Model):
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=255, null=True, blank=True)
    genre = models.CharField(max_length=255, null=True, blank=True)
    tags = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    understanding = models.IntegerField(null=True, blank=True)
    accuracy = models.CharField(max_length=50, null=True, blank=True)
    user_count = models.IntegerField(null=True, blank=True)
    views = models.IntegerField(null=True, blank=True)
    img_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    chatbot = models.ForeignKey(Novel, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('novel', 'user')  # 1 review max par user/novel

    def __str__(self):
        return f'Review by {self.user.username} for {self.novel.name}'
