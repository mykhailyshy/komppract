# tasks/models.py
from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    
    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)  # Опис завдання
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='New')
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)  # Випадаючий список з варіантами
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({dict(self.PRIORITY_CHOICES).get(self.priority)})"
