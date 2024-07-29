from django.db import models
from django.utils import timezone

class ChatRoom(models.Model):
    name = models.CharField(max_length=255, default='General Chat Room')

    def __str__(self):
        return self.name

class Message(models.Model):
    room = models.ForeignKey(ChatRoom, related_name='messages', on_delete=models.CASCADE, default=1)  # Assuming the default room has an ID of 1
    content = models.TextField(default='No content')
    timestamp = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=255, default='Anonymous')

    def __str__(self):
        return f'{self.author}: {self.content[:20]}'
