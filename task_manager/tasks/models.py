from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[('new', 'Нове'), ('in_progress', 'В процесі'), ('completed', 'Завершено')])
    priority = models.CharField(max_length=20, choices=[('low', 'Низький'), ('medium', 'Середній'), ('high', 'Високий')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
