# myapp/models.py
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.created_at}"
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    gamer_tag = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.gamer_tag} ({self.email})"
class FavoriteGame(models.Model):
    created_by = models.CharField(max_length=100)  # changed from gamer_name
    title = models.CharField(max_length=100)  # changed from game_title
    genre = models.CharField(max_length=50, blank=True)  # added genre
    description = models.TextField(blank=True)  # added description for detailed info
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_by} - {self.title}"