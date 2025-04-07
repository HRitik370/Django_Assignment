from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='liked_answers', blank=True)
    
    def __str__(self):
        return f"Answer to: {self.question.title[:30]}"
    
    def total_likes(self):
        return self.likes.count()
    
    class Meta:
        ordering = ['-created_at']